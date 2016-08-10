#!/usr/bin/env python
print "Content-Type: text/html"
print

import os
import cgi
import sys
import json

print "Parsing...",
payload = json.load(sys.stdin)
print "OK"

repo = payload['repository']['name']
branch = payload['ref'].split('/')[2]

print "Repo: " + repo
print "Branch: " + branch

if repo == "uw-homepage" and branch == "master":
    os.system("git pull")
    print "OK"
