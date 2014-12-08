# -*- coding: utf-8 -*-
from twython import Twython
import time

API_KEY = 'XXXXXXXXXXXXXXXX'
API_SECRET = 'XXXXXXXXXXXXXXXX'
ACCESS_TOKEN = 'XXXXXXXXXXXXXXXX'
ACCESS_TOKEN_SECRET = 'XXXXXXXXXXXXXXXX'

twitter = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#twitter.update_status(status= "")

filename=open('lines.txt', 'r')
f=filename.readlines()
filename.close()

for line in f:
    twitter.update_status(status=line)
    time.sleep(1)

print "DONE!"

