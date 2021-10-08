class TimeoutMsg:
	def __init__(self, tmo_info, last_round_tc, high_commit_qc):
		self.tmo_info  = tmo_info
		self.last_round_tc = last_round_tc
		self.high_commit_qc = high_commit_qc
		printf('Created new TimeoutMsg class')