#!/usr/bin/env python3

# imports
import os
import pkg_resources
from importlib import import_module

INDEX_FILE = 'modindex.txt'

client_commands = {}
server_commands = {}

def client_handler(cmd):

    def decorate(func):
        client_commands[cmd] = func
    return decorate


def server_handler(cmd):

    def decorate(func):
        server_commands[cmd] = func
    return decorate

def load_modules():

    for fname in pkg_resources.resource_string(__name__, INDEX_FILE).split():
        if fname.endswith('.py'):
            mod = os.path.splitext(fname)[0]

            if mod == '__init__':
                continue
            elif mod in server_commands.keys():
                raise Exception('duplicate module detected: {}'.format(mod))
            
            import_module('modules.' + mod)

