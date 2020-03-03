from twilio.rest import Client
from private import smsconfig

class Sms:
	def __init__(self):
		self._apiKey = smsconfig['apikey']
		self._apiSecret = smsconfig['apisecret']
		self.client = Client(self._apiKey, self._apiSecret)

	def sendSms(self,data):
		msg = self.client.messages.create(body="ALERT"+data+smsconfig['message'], from_=smsconfig['from'], to=smsconfig['to'])