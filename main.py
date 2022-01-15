import blockchain
import transaction
from generator import Generator

b = blockchain.Blockchain()
g = Generator()

users = []
for i in range(6):
	users.append(g.generate_random_public_key())

tx1 = transaction.Transaction(users[0],users[3],500)
tx2 = transaction.Transaction(users[1],users[4],350)
tx3 = transaction.Transaction(users[2],users[5],200)

b.addNode(tx1)
b.addNode(tx2)
b.addNode(tx3)

print(b)