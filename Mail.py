import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

from private import mailconfig,messageconfig

class Mail:
	def __init__(self):
		self.addr = mailconfig['addr']
		self.mdp = mailconfig['password']
		self.s = smtplib.SMTP(host=mailconfig['host'], port=mailconfig['port'])
		self.s.ehlo()
		self.s.starttls()
		self.s.ehlo()
		self.s.login(self.addr, self.mdp)

	def sendMail(self, data):
		e = 'UTF-8'
		typetext = 'plain'
		msg = MIMEText(messageconfig['message'], typetext, _charset=e)

		msg['From'] = self.addr
		msg['To'] = messageconfig['mail']
		msg['Subject'] = "CryptoPush: ALERT "+data
		msg['Date'] = formatdate(localtime=True)
		msg['Charset'] = e
		msg['Content-Type'] = 'text/'+typetext+'; charset='+e
		msg['X-Priority'] = '1'
		self.s.send_message(msg)