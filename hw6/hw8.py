from hotqueue import HotQueue
import uuid
import redis
import datetime
import json

q = HotQueue("queue", host='172.17.0.1', port=6379, db=1)
rd = redis.StrictRedis(host='172.17.0.1', port=6379, db=0)

def generate_jid():
    return str(uuid.uuid4())

def _generate_job_key(jid):
    return 'job.{}'.format(jid)

def _save_job(job_key, job_dict):
    """Save a job object in the Redis database."""
    rd.set(job_key, json.dumps(job_dict))
    return 1

def queue_job(job_key):
    """Add a job to the redis queue."""
    q.put(job_key)
    return 2

def _create_job(jid, status, start, end, start_time, updated_time):
    """Creates a job with specified parameters"""
    if isinstance(jid, str):
        return {'id': jid,
                'status': status,
                'start': start,
                'end': end,
                'start time': start_time,
                'updated time': updated_time}

    return {'id': jid.decode('utf-8'),
            'status': status.decode('utf-8'),
            'start': start.decode('utf-8'),
            'end': end.decode('utf-8'),
            'start time': start_time.decode('utf-8'),
            'updated time': updated_time.decode('utf-8')}

def add_job(start, end, status="submitted"):
    """Add a job to the redis queue."""
    jid = generate_jid()
    job_key = _generate_job_key(jid)
    start_time = str(datetime.datetime.now())
    job_dict = _create_job(jid, status, start, end, start_time, start_time)
    _save_job(job_key, job_dict)
    queue_job(job_key)
    return json.dumps(job_dict)

def get_job(jid):
    """Gets job from redis db using jid and returns job_dict"""
    result = json.loads(rd.get(_generate_job_key(str(jid))))
    return result

def get_all_jobs():
    """Gets all jobs from redis db and presents job_dicts in a list"""
    results = []
    for k in rd.keys():
        results.append(json.loads(rd.get(k)))
    return results

def update_job_status(jid, new_status):
    """Update the status of job with job id `jid` to status `new_status`."""
    job_content = json.loads(rd.get(_generate_job_key(str(jid))))
    updated_time = str(datetime.datetime.now())
    job_content["updated time"] = updated_time
    job_content["status"] = new_status
    _save_job(_generate_job_key(str(jid)), job_content)
