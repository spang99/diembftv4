class TimeoutInfo:
	def __init__(self, round, high_qc, sender):
		self.round  = round
		self.high_qc = high_qc
		self.sender = sender
		self.signatiure = signing_key.sign((round, high_qc.round))
		printf('Created new TimeoutInfo class')