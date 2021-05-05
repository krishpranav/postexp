IP = 127.0.0.1
DELAY = 1
PORT = -p 8081
PYTHON = python2.7

CL = postexp/client.py
SV = postexp/server.py

# debug mode helpers

# run client at localhost:8081, delay 1s
cl: dbg
	$(PYTHON) $(CL) $(IP) $(DELAY) $(PORT) --no-selfdestruct

# run client at localhost:8081, delay 1s, verbosely
clv: dbg
	$(PYTHON) $(CL) $(IP) $(DELAY) $(PORT) --debug --no-selfdestruct

# run server on localhost:8081
sv: dbg
	$(PYTHON) $(SV) $(PORT)