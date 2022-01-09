from transaction import Transaction

class Node:

	__transaction: Transaction = None
	__previousHash: str = None

	def __init__(self, transaction, previousHash):
		self.__transaction = transaction
		self.__previousHash = previousHash

	def getPreviousHash(self):
		return self.__previousHash

	def getTransaction(self):
		return self.__transaction
	
	def getHashBasis(self):
		basis = ""
		basis += self.__previousHash
		basis += self.__transaction.getBasis()

		return basis