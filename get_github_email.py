#!/usr/bin/env python3
# @Author:	Leeroy P. Williams
# @Date:	30/05/19
# @Desc:	Use the following script in order to get a github users email address.
#			The only requirement is that you will need to know the [users] user-name.
#			Should you want to contant them.

import requests


username = input("Enter username: ")
url = "https://api.github.com/users/{}/events".format(username)

def main():
	getEmail(username)

def getEmail(username):
	"""
		This function is responsible for traversing the API to find the user email address.
	"""
	res = requests.get(url)
	data = res.json()			# The data found within the github API is stored as JSON content, so we need to decode it

	for i in data:
		if "payload" in i:
			for j in i["payload"]:
				if j == "commits":
					user_email = i["payload"][j][0]["author"]["email"]	# Print ut the email address located in the dictionary
	print("Email: {}".format(user_email))

if __name__ == "__main__":
	main()