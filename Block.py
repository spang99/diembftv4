class Block:
	def __init__(self, author, round, payload, qc, id):
		self.auhor = author
		self.round  = round
		self.payload = payload
		self.qc = qc
		self.id = id
		printf('Created new Block class')