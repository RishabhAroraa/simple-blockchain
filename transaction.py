class Transaction:

	__sender: str = None
	__receiver: str = None
	__amount: int = None

	def __init__(self, sender, receiver, amount):
		self.__sender = sender
		self.__receiver = receiver
		self.__amount = amount

	def get_sender(self):
		return self.__sender

	def get_receiver(self):
		return self.__receiver

	def get_amount(self):
		return self.__amount

	def get_basis(self):
		basis = ""
		basis += self.__sender
		basis += self.__receiver
		basis += str(self.__amount)

		return basis
