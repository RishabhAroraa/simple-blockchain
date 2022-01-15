import random
import hashlib

class Generator:

	__nonce = None

	def __init__(self):
		self.__nonce = random.randint(0,10000001)

	def generate_random_public_key(self):
		random_number = random.randint(0,10000001)
		random_string = str(random_number) + str(self.__nonce)
		return hashlib.sha256(random_string.encode()).hexdigest()