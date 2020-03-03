#!/usr/bin/env python
from meraki_api import meraki_api
from webexBot import webexBot

import sys
import json
import time

def main():
	data = None
	api = None
	webex = None
	device_ports = "all"	# comma delimittted list of ports to check for line speed (or set to "all")
	filter = "devices"		# options: organization, network, devices (where devices is a list of serials provided by command line in a file)
	action = None
	f = None				# file handle

	# Try (optional) webex:
	try:
		webex = webexBot()
	except:
		webex = None
	# Try to setup the api
	try:
		api = meraki_api()

	except:
		print "Couln't initialize the API framework or Webex."
		exit(1)

	if filter == "devices":
		# Get a list of devices as a file passed in sys.argv[1]
		try:
			devices = sys.argv[1]
			f = open(devices,"r")
		except:
			print "Could not open device list file."
			exit(2)

		# Read the file, set the action, and report the line speeds
		output_cli = ""
		output_webex = ""

		for serial in f:
			sSerial = serial.strip()
			timeAgo = int(time.time() - (60 * 60 * 60))
			action = "devices/" + sSerial + "/switchPortStatuses?t0=" + str(timeAgo)
			data = api.readData(action)

			# Parse the data show port/linespeed
			ports = device_ports.split(",")

			for entry in data:
				if device_ports != "all":
					if entry["portId"] in ports:
						output_cli+="Switch: " + sSerial + " | Port " + entry["portId"] + " linespeed: " + entry["speed"] + "\n"
						if(webex!=None):
							output_webex+="Switch: " + sSerial + " | Port " + entry["portId"] + " linespeed: " + entry["speed"]+ "  \n"
				else:
					output_cli+="Switch: " + sSerial + " | Port " + entry["portId"] + " linespeed: " + entry["speed"] + "\n"
					if (webex!=None):
						output_webex+="Switch: " + sSerial + " | Port " + entry["portId"] + " linespeed: " + entry["speed"]+ "  \n"
			print output_cli
			if (webex!=None):
				webex.sendMsg(output_webex)
		f.close()

	elif filter == "network":
		print ("Todo")

	elif filter == "organization":
		# Get all device serials
		f = None
		try:
			f = open("organization.id","r")
		except:
			print "No organization.id file found to specify the ORG ID to send the API request to."
			print "Please add your organization ID to this file in the same directory as the script, and run it again."
			exit(3)
		orgId = f.read().strip()

		action = "organization/" + orgId + "/devices"
		data = api.readData(action)
		print(data)

if __name__ == "__main__":
	main()
