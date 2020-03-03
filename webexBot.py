"""
	Description:
		Class Object Definition file for easy use of a webex bot.

	Requires:
		Bot ID and Token for authorization of posts. Can be found at https://developer.webex.com/
		Checks the local directory for webex_bot.id, webex_room.id, and webex_bot.token

	Author:
		John Thorne
"""

""" Imports """
import requests # for HTTPS GET/POST function calls
import json		# for formatting and storing data structures for GET/POSTS

class webexBot:
	room_id = None
	api_url = None
	bot_token = None

	def __init__(self, apiVersion="v1", apiUrl="https://api.ciscospark.com"):
		self.api_URL = apiUrl + "/" + apiVersion

		try:
			f = open("webex_room.id","r")
			self.room_id=f.read().strip()
			f.close()

			f = open("webex_bot.token","r")
			self.bot_token=f.read().strip()
			f.close()
		except:
			print "Couldn't load the webex_room.id or webex_bot.token files for webex integration."
			exit(3)

	# Post a message in markdown format to webex room configured for the bot
	# Example msg: ""<@all> : [$NODE_NAME]($NODE_LINK) has missed $THRESHOLD consecutive pings from dashboard."
	def sendMsg(self, msg):
		try:
			myData = {
				"roomId":self.room_id,
				"markdown":msg
			}
			val = requests.post(self.api_URL+"/messages", myData, headers = {"Authorization": "Bearer "+self.bot_token})
			return True
		except:
			return False
