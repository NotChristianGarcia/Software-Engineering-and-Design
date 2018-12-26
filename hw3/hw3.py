"""
Author: Christian R. Garcia
Creates a flask server with different routes that allows to to call data from
HW1's functions to read the "sunspots.csv" file.

Run with "python3 hw3.py"
"""
import sys
from flask import Flask, jsonify, request
sys.path.append('../hw1')
sys.path.append('../hw8')
from hw1 import csvDataReaderf, csvDataReaderg, csvDataReaderh
import hw8
import json

csvFile = "../hw1/sunspots.csv"
app = Flask(__name__)


@app.route('/spots', methods=['GET'])
def get_dataWArgs():
    """
    This functions takes arguments in the form of "addr/spots?start=1994&limit=2"
    Takes 2 arguments at a time, either start and end or limit and offset, will
    throw a 400 otherwise and notify the user of the error in the form of a json
    string.
    """
    start = request.args.get('start')
    end = request.args.get('end')
    limit = request.args.get('limit')
    offset = request.args.get('offset')

    if start is None:
        start = 0
    try:
        start = int(start)
    except TypeError:
        return jsonify("Input for 'start' was not an int"), 400

    if end is None:
        end = 0
    try:
        end = int(end)
    except TypeError:
        return jsonify("Input for 'end' was not an int"), 400

    if limit is None:
        limit = 0
    try:
        limit = int(limit)
    except TypeError:
        return jsonify("Input for 'limit' was not an int"), 400
    if limit < 0:
        return jsonify("Input for 'limit' must be 0 or a positive int"), 400

    if offset is None:
        offset = 0
    try:
        offset = int(offset)
    except TypeError:
        return jsonify("Input for 'offset' was not an int"), 400
    if offset < 0:
        return jsonify("Input for 'offset' must be 0 or a positive int"), 400

    if (start or end) and (limit or offset):
        return jsonify("Start and end can only be used independently from limit and offset"), 400
    elif start or end:
        if start is 0:
            start = -10000
        elif end is 0:
            end = 100000000
        return jsonify(csvDataReaderg(csvFile, start, end))
    elif limit or offset:
        if limit is 0:
            limit = 100000000
        elif offset is 0:
            offset = 0
        return jsonify(csvDataReaderh(csvFile, limit, offset))
    else:
        return jsonify(csvDataReaderf(csvFile))


@app.route('/spots/<idInp>', methods=['GET'])
def get_ID(idInp):
    """
    Will take an id in the route and provide the dict associated with the id in the dataset.
    """
    try:
        idInp = int(idInp)
    except TypeError:
        return jsonify("The id provided is invalid"), 400

    return jsonify(csvDataReaderf(csvFile)[idInp])


@app.route('/spots/years/<year>', methods=['GET'])
def get_year(year):
    """
    Will take the year in the route and provide the dict associated with the year in the dataset.
    """
    try:
        year = int(year)
    except TypeError:
        return jsonify("The year provided is invalid"), 400

    return jsonify(csvDataReaderg(csvFile, year, year)[0])

@app.route('/jobs', methods=['POST'])
def post_job():
    """Words"""
    post_data = json.loads(request.get_data().decode("utf-8"))
    print(type(post_data))
    if post_data:
        if "start" in post_data:
            start = post_data["start"]
        else:
            start = None

        if "end" in post_data:
            end = post_data["end"]
        else:
            end = None

        if "limit" in post_data:
            limit = post_data["limit"]
        else:
            limit = None

        if "offset" in post_data:
            offset = post_data["offset"]
        else:
            offset = None

        if start is None:
            start = 0
        try:
            start = int(start)
        except TypeError:
            return jsonify("Input for 'start' was not an int"), 400

        if end is None:
            end = 0
        try:
            end = int(end)
        except TypeError:
            return jsonify("Input for 'end' was not an int"), 400

        if limit is None:
            limit = 0
        try:
            limit = int(limit)
        except TypeError:
            return jsonify("Input for 'limit' was not an int"), 400
        if limit < 0:
            return jsonify("Input for 'limit' must be 0 or a positive int"), 400

        if offset is None:
            offset = 0
        try:
            offset = int(offset)
        except TypeError:
            return jsonify("Input for 'offset' was not an int"), 400
        if offset < 0:
            return jsonify("Input for 'offset' must be 0 or a positive int"), 400

        if (start or end) and (limit or offset):
            return jsonify("Start and end can only be used independently from limit and offset"), 400
        elif start or end:
            if start is 0:
                start = -10000
            elif end is 0:
                end = 100000000
            return hw8.add_job(start, end) + "\n"
        elif limit or offset:
            if limit is 0:
                limit = 100000000
            elif offset is 0:
                offset = 0
            start_year = 1770
            start = start_year + offset
            end = start + limit
            return hw8.add_job(start, end) + "\n"
    return hw8.add_job(-10000, 100000000)+ "\n"


@app.route('/jobs', methods=['GET'])
def get_all_jobs():
    return jsonify(hw8.get_all_jobs())


@app.route('/jobs/<job_id>', methods=['GET'])
def get_one_job(job_id):
    result = hw8.get_job(job_id)
    if result is None:
        return jsonify("Job id supplied led to not hits in our database, please try again."), 400
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
