#!/usr/bin/env python
from meraki_api import meraki_api

def main():
	print "Hello Meraki API Framework!"

	api = meraki_api()
	organizations = api.readData("organizations")
	for org in organizations:
		print org["name"] + "\tid: " + str(org["id"])

if __name__ == "__main__":
	main()
