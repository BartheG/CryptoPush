from coinbase.wallet.client import Client

class WrapCoinbase:
	def __init__(self):
		self._apiKey = "d43df01efef7f09817cb72534d5ce6e4fe06a4cfc5a3220bba3092fb9f9ba699"
		self._apiSecret = "c802d8303a5f7058046f697c7aae38a31b902ff61dd1b9c5c757ccd9a414a9ca"
		self.client = Client(self._apiKey, self._apiSecret)

	def getSellPrice(self, name):
		return self.client.get_sell_price(currency_pair = name+'-EUR')