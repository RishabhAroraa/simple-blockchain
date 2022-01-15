from transaction import Transaction

class Block:

	__transaction: Transaction = None
	__previous_hash: str = None

	def __init__(self, transaction, previous_hash):
		self.__transaction = transaction
		self.__previous_hash = previous_hash

	def get_previous_hash(self):
		return self.__previous_hash

	def get_transaction(self):
		return self.__transaction
	
	def get_hash_basis(self):
		basis = ""
		basis += self.__previous_hash
		basis += self.__transaction.get_basis()

		return basis