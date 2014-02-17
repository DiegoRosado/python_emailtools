#!/usr/bin/python
import sys
import os
import argparse
import getpass

import config
from emailtools import EmailServer, Email

#Reading config from file
server_url = config.server_url
port = config.smtp_port
ssl = config.ssl
email_sender = config.email_sender
email_destination = config.email_destination
username = config.username

#harcoded config. (It will be moved to other config file)
mime_type = 'plain'
subject = "This is a test"
body = "This is my body"

#password must have to be typed (so far) to avoid leaking passwords
password = getpass.getpass("Type your password:")

def main():
	try:
		email = Email(mime_type, body, subject, email_sender)
		email_server = EmailServer(server_url, port, ssl)
		email_server.sendmail(username, password, email_sender, email_destination, email)
	except Exception, exc:
		sys.exit( "mail failed; %s" % str(exc) ) # give a error message


if __name__ == '__main__':
    main()


