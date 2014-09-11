# -*- coding: utf-8 -*-
from twython import Twython
import time

API_KEY = 'XXXXXXXXXXXXXXXX'
API_SECRET = 'XXXXXXXXXXXXX'
ACCESS_TOKEN = 'XXXXXXXXXXXXX'
ACCESS_TOKEN_SECRET = 'XXXXXXXXXXXXX'

twitter = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#twitter.update_status(status= "")

filename=open('helloworld.txt', 'r')
f=filename.readlines()
filename.close()

#there's a problem here
for line in f:
	if len(line) < 140:
    		twitter.update_status(status=line)
        	time.sleep(3)
