#!/usr/bin/env python
print "Content-Type: text/html"
print

import os
import cgi
import json

form = cgi.FieldStorage()
json_payload = form.getvalue('payload')
payload = json.loads(json_payload)

script_dir = os.path.join(os.curdir, 'scripts')
repo = payload['repository']['name']
branch = payload['ref'].split('/')[2]

os.system("git pull")
