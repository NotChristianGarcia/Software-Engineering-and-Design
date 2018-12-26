## Homework Six.

### Instructions
	Docker repo url is: https://hub.docker.com/r/notchristiangarcia/hw6/
	To pull the docker repo, use: docker pull notchristiangarcia/hw6:v1

### Information
	When you run the docker image you'll get a flask server identical to that
	of hw3.py. When you make calls to it, on whatever port you specified in
	your .yml, you'll receive back jsonified data.

### Calls
	addr/spots
		Return list of all dicts

	addr/spots?start=<year>&end=<end>
		Returns list of dicts from year start to year end

	addr/spots?offset=<offset>&limit=<limit>
		Returns list of dicts from offset id until offset id + limit

	addr/spots/<id>
		Returns dict from list based on id inputted.

	addr/spots/years/<year>
		Returns dict from list based on year inputted.
