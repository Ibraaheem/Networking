#!/usr/bin/env python3

# @Author:	Leeroy P. Williams
# @Date:	
# @Desc: 	This module shall be called out to locate a github users email address,
#		 	from the github api. Thus removing the need to manually locate it.

import json
import urllib.request


def main():
	
	iterdict()

def scrapePage(url_link):
	"""
		This function takes an argument of the URL that we wish to access.
		This being the https://api.github.com/users/[USERNAME]/events/public link.
		It will then display only the index that contains the data that we are looking for.
	"""
	URL = url_link
	try:
		# Check if the page is valid and connects
		page = urllib.request.urlopen(URL)						
		print("[+] Connection to: [{}] verified".format(URL))

		# Scrape the Webpage

		# api.github.com uses JSON format to display its data,
		# so we load the page contents to json.load()
		data = json.load(page)

		# Recursive function to iterate through the dict
		iterdict(data[2])
		
	except Exception:
		print("[-] There was a problem with the url you provided: {}".format(URL))
	
def iterdict(d):
	"""
		Iterate over the dictionary contents recursively should the dictionary,
		contain more than one nested file.
	"""

	values = []			# Keep the dictionary values so that we can remove the ones we don't need
	email = []
	for value in d.items():
		if isinstance(value, dict):
			iterdict(value)
		else:
			values.append(value)

	# This index point is where we find the email address
	temp = list(values[4])
	email_locaton = temp[1]

	for v in temp[1].items():
		if isinstance(v, dict):
			iterdict(v)
		else:
			email.append(v)

	temp2 = list(email[-1])

	email2 = []
	for i in temp2[1][0].items():
		if isinstance(i, dict):
			iterdict(i)
		else:
			email2.append(i)

	# Display the email address extracted
	temp3 = list(email2)
	email_address = list(temp3[1])[1]["email"]
	print(email_address)

if __name__ == "__main__":
	main()