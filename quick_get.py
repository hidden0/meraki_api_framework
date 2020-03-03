#!/usr/bin/env python
from meraki_api import meraki_api
import sys
import json

def main():
	data = None
	api = None

	try:
		api = meraki_api()
		data = api.readData(sys.argv[1])
	except:
		print "Bad action passed as argument #1."
		exit(1)

	print data

if __name__ == "__main__":
	main()
