import nacl.encoding
import nacl.hash

class LedgerCommitInfo:
	def __init__(self, commit_state_id, vote_info):
		self.commit_state_id = id
		self.vote_info_hash  = nacl.hash.sha256(msg, encoder=nacl.encoding.HexEncoder)