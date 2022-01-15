from transaction import Transaction
from block import Block

import hashlib

class Blockchain:

	__nodes: list[Block] = []; 


	def __init__(self):

		genesis_hash = hashlib.sha256("".encode()).hexdigest()

		self.__genesis_node = Block(Transaction("None","None",0),genesis_hash)
		self.__nodes.append(self.__genesis_node)
		

	def addNode(self, tx: Transaction):
		basis = self.__nodes[-1].get_hash_basis()

		hash = hashlib.sha256(basis.encode()).hexdigest()
		node = Block(tx, hash)

		self.__nodes.append(node)
	
	def __repr__(self) -> str:
		result = ""
		for node in self.__nodes:
			result += ("Transaction: \n\tFrom: 0x{} \n\tTo: 0x{} \n\tAmount: {} \n\tBlock Hash: 0x{} \n\n".format(
				node.get_transaction().get_sender(),
				node.get_transaction().get_receiver(),
				node.get_transaction().get_amount(),
				node.get_previous_hash()
			))
		
		return result
