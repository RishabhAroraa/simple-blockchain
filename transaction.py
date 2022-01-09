class Transaction:

	__sender: str = None
	__receiver: str = None
	__amount: int = None

	def __init__(self, sender, receiver, amount):
		self.__sender = sender
		self.__receiver = receiver
		self.__amount = amount

	def getSender(self):
		return self.__sender

	def getReceiver(self):
		return self.__receiver

	def getAmount(self):
		return self.__amount

	def getBasis(self):
		basis = ""
		basis += self.__sender
		basis += self.__receiver
		basis += str(self.__amount)

		return basis
