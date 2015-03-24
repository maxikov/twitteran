#!/usr/bin/env python
# -*- coding: utf8 -*-

import pickle


dumpfile = open("statuses.pkl", "rb")
statuses = pickle.load(dumpfile)
dumpfile.close()

for status in statuses:
	print status.text
	print [str(tag.text) for tag in status.hashtags]
	print status.created_at
	print "\n\n"
