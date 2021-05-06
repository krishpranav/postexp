#!/usr/bin/env python3

# imports
import module


MODNAME = 'template'
USAGE = """Brief description of module.
usage: template [-h] args go here etc
\noptions:
-h\t\tshow help"""


@module.server_handler(MODNAME)
def server(server, argv):
    print 'template module',
    pass


@module.client_handler(MODNAME)
def client(client, inp):
    pass
