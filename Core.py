import argparse

import WrapCoinbase, Mail, Sms

class Core:
	def __init__(self):
		parser = argparse.ArgumentParser()
		parser.add_argument(
			"-w",
			"--towatch",
			required=True,
			help="Crypto to watch! - Ex: -w \"BTC ZRX\""
		)
		parser.add_argument(
			"-v",
			"--value",
			help="Value of trigger! - Ex: -v \"BTC:1200 ZRX:8\""
		)
		parser.add_argument(
			"-c",
			"--contact",
			help="Contact method - Ex: -c \"SMS\" or -c \"MAIL\"",
			required=True
		)
		self.cryptoTab = {
			'ZRX': 27,
			'BCH': 170,
			'BTC': 120
		}
		self.args = parser.parse_args()
		self.getCryptoToWatch()
		self.getTriggersValues()
		self.WCoinBase = WrapCoinbase.WrapCoinbase()
		self.WMail = Mail.Mail()
		self.WSms = Sms.Sms()
		self.cMethod = self.getContactMethod()
		if len(self.cMethod)<=0:
			print('Error: Contact method not available')
			raise ValueError

	def getContactMethod(self,):
		equiv_contact = {
			'mail':self.WMail.sendMail,
			'sms':self.WSms.sendSms}
		t_contact = self.args.contact.split(' ')
		return [ equiv_contact[i.lower()] for i in t_contact\
			if i.lower() in equiv_contact.keys() ]

	def getCryptoToWatch(self):
		self.CryptoTW = self.args.towatch.split(' ')
		for i in self.CryptoTW:
			if i not in self.cryptoTab.keys():
				self.CryptoTW.remove(i)

	def checkCrypto(self, data):
		self.formatSellPrice(self.WCoinBase.getSellPrice(data))
		if self.cryptoTab[data] < float(self.sellPrice['amount']):
			return True
		return False

	def getTriggersValues(self):
		if self.args.value is None:
			return
		val = self.args.value.split(' ')
		for i in val:
			if i.find(':') is not -1:
				data = i.split(':')
				self.cryptoTab[data[0]] = data[1]

	def formatSellPrice(self, data):
		self.sellPrice = {
			'name': data['base'],
			'amount': data['amount'],
			'unit': data['currency']
		}

	def loop(self):
		[ i_contact(i) for i in self.CryptoTW\
			for i_contact in self.cMethod\
				if self.checkCrypto(i) is True ]