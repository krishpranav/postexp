# postexp
A simple post exploition tool

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

# Installation
```
git clone https://github.com/krishpranav/postexp
cd postexp
make
```

# Usage:

- terminal 1

```
./postexp-client 127.0.0.1 1 --debug --no-selfdestruct
```

- terminal 2

```
sudo ./postexp-server
```

# client
```
$ ./postexp-client -h
usage: postexp-client [-h] [-p PORT] [--debug] [--no-daemon] [--no-selfdestruct]
                   IP [INTERVAL]

positional arguments:
  IP                    Poet Server
  INTERVAL              Beacon Interval, in seconds. Default: 600

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT
  --debug               show debug messages. implies --no-daemon
  --no-daemon           don't daemonize
  --no-selfdestruct     don't selfdestruct
```

# server
```
$ ./postexp-server -h
usage: postexp-server [-h] [-p PORT] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT
  -v, --version         prints the Poet version number and exits
```
