"""
	Description:
		Class Object Definition file for Meraki API interaction.

	Author:
		John Thorne
"""
""" Imports """
import requests # for HTTPS GET/POST function calls
import json		# for formatting and storing data structures for GET/POSTS

"""Globals"""

APIURL = "https://api.meraki.com/api"
APIVERSION = "v0"

"""
Base class for setting up meraki API interaction.
The constructor demands that an API key be provided for interactions.
"""
class meraki_api:
	# Fields of the API
	api_key = ""
	api_url = APIURL
	api_version = APIVERSION

	# Constructor
	def __init__(self, keyFile="api.cred"):
		# Try to read the local .cred file if it exists
		try:
			f = open(keyFile,"r")
			self.api_key=f.read().strip()
		except:
			print "Could not open " + keyFile
			exit(1)

	# Set/get methods
	def get_api_key(self):
		return self.api_key
	def get_api_url(self):
		return self.api_url
	def get_api_version(self):
		return self.api_version
	def get_api_action(self):
		return self.api_action

	def set_api_key(val):
		self.api_key = val
	def set_api_url(val):
		self.api_url = val
	def set_api_version(val):
		self.api_version = val
	def set_api_action(val):
		self.api_action = val

	# GET/POST/PUT calls.
	# GET is read, POST is new/create, PUT is update
	"""
		readData(self, action)
			- action is the string to GET after combining the full API URL and Version together
	"""
	def readData(self, action):
		# Setup the request
		added_headers = {'X-Cisco-Meraki-API-Key': self.api_key, 'Content-Type': 'application/json'}
		request_url = self.api_url + "/" + self.api_version + "/" + action
		try:
			api_response = requests.get(url = request_url, headers=added_headers)
			return json.loads(api_response.text)
		except:
			return "Error in readData function." # failure
	"""
		postNew(self, action, )
			- action is the string to GET after combining the full API URL and Version together
	"""
	def postNew(self, action):
		# Setup the request
		added_headers = {'X-Cisco-Meraki-API-Key': self.api_key, 'Content-Type': 'application/json'}
		request_url = self.api_url + "/" + self.api_version + "/" + action

		api_response = requests.get(url = request_url, headers=added_headers)
		return json.loads(api_response.text)
