from transaction import Transaction
from node import Node

import hashlib

class Blockchain:

	__nodes: list[Node] = []; 

	def __init__(self):
		self.__genesisNode = Node(Transaction("","",0),"")
		self.__nodes.append(self.__genesisNode)
		

	def addNode(self, tx: Transaction):
		basis = self.__nodes[-1].getHashBasis()

		hash = hashlib.sha256(basis.encode()).hexdigest()
		node = Node(tx, hash)

		self.__nodes.append(node)
	
	def __repr__(self) -> str:
		result = ""
		for node in self.__nodes:
			result += ("Transaction: {} -> {} for {} | Hash: {} \n".format(
				node.getTransaction().getSender(),
				node.getTransaction().getReceiver(),
				node.getTransaction().getAmount(),
				node.getPreviousHash()
			))
		
		return result
