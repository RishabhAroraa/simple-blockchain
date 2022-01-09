import blockchain
import transaction

b = blockchain.Blockchain()

tx1 = transaction.Transaction('alice','bob',500)
tx2 = transaction.Transaction('bob','charlie',350)
tx3 = transaction.Transaction('bob','dwight',2400)

b.addNode(tx1)
b.addNode(tx2)
b.addNode(tx3)

print(b)