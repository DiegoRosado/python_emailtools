"""

author: Diego Rosado

Tools for email

"""

from smtplib import SMTP, SMTP_SSL as SSMTP
from email.MIMEText import MIMEText


class EmailServer(object):

    def __init__(self, server_url, port, ssl=True):
        self.server_url = server_url
        self.port = port
        self.ssl = ssl
    
    def __getConnection(self):
        if (self.ssl):
            conn = SSMTP(self.server_url)
        else:
            conn = SMTP(self.server_url)
        return conn
            
    def sendmail(self, username, password, source, destination, email):
        conn = self.__getConnection()
        conn.set_debuglevel(True)
        conn.login(username, password)
        try:
            conn.sendmail(source, destination, email.as_string())
        finally:
            conn.close()

class Email(object):
    
    def __createMimeType(self, mime_type, body):
        if mime_type == 'plain':
            return MIMEText(body, mime_type)
        elif mime_type == 'html':
            raise NotImplementedError("Not implemented yet. Feel free to do it  ;-) ")
        elif mime_type == 'xml':
            raise NotImplementedError("Not implemented yet. Feel free to do it  ;-) ")
        else:
            raise ValueError(("%s is not a valid mime type" % mime_type))


    def __init__(self, mime_type, body, subject, email_sender):
        self.message = self.__createMimeType(mime_type, body)
        self.message['Subject'] = subject
        self.message['From'] = email_sender
        
    def as_string(self):
        return self.message.as_string()


