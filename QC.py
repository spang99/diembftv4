class QC:
	def __init__(self, vote_info, ledger_commit_info, signatures, author):
		self.vote_info = vote_info
		self.ledger_commit_info  = ledger_commit_info
		self.high_commit_qc = high_commit_qc
		self.signatures = signatures
		self.author = sender
		self.author_signature = signing_key.sign(signatures)
		printf('Created new QC class')