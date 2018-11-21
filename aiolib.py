# -*- coding: utf-8 -*-


import asyncio
from aiohttp import web, WSMsgType
import aiofiles

import sys
import os
import os.path
from urllib.parse import urlparse, parse_qs
import json

from io import StringIO

route = {}

def add_get(*args, **kwargs):
    def decorator(f):
        if len(args) == 0 or not args[0]:
            path = f.__module__.__name__.replace('.','/') + f.__name__
        else:
            path = f.__module__.__name__.replace('.','/') + args[0]
        route[path] = f
        print('add_get({},{})'.format(path,f))
    return decorator
        
