#!/usr/bin/python
# -*- coding: utf-8 -*-

import xport

with open('DEMO_I.xpt', 'rb') as f:
	reader = xport.Reader(f)
	print(reader.fields)
	# for row in xport.Reader(f):
		# print(row)
