#!/usr/bin/env python
# -*- coding: utf8 -*-

import twitter
import pickle

CONSUMER_KEY = 'nvHkjbdhV4PI9WrYdpqaSmmT5'
CONSUMER_SECRET ='kNEg2zwBaBNQOug3yaQ5r0r0aqXHrMJdTEUvps9a3byG7bVppK'
OAUTH_TOKEN = '85889667-BNUJlo9r8KeA8CXPwkGm3mPkuBD634bUH8QVyQ2tG'
OAUTH_TOKEN_SECRET = 'nKijMpWwDEHmWD7mIWtMhdtIRc4KQo59MvcnQF5ffsdxJ'

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


f = open("/mnt/data/twitterdump/dump_mar_31_9_10", "w", 0)

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

	def on_data(self, data):
		print data
		f.write(str(data))
		return True

	def on_error(self, status):
		print status


if __name__ == '__main__':


	while True:
		try:

			#This handles Twitter authetification and the connection to Twitter Streaming API
			l = StdOutListener()
			auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
			auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
			stream = Stream(auth, l)


			stream.filter(track=['rain', 'thunder', 'lightning', 'hurricane', 'storm', 'hail', 'snow', 'flood', 'cloud', 'overcast', 'shower'])
		except Exception as e:
			print e

