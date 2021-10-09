from PaceMaker import PaceMaker


class LeaderElection:
    def __init__(self, validators, window_size, exclude_size, reputation_leaders):
        self.validators = validators
        self.window_size = window_size
        self.exclude_size = exclude_size
        self.reputation_leaders = reputation_leaders

    def elect_reputation_leader(self, qc):
        active_validators = {}
        last_authors = {}
        current_qc = qc
        i = 0
        while (i < self.window_size) or len(last_authors) < self.exclude_size:
            current_block = Ledger.committed_block(current_qc.vote_infor.parent_id)
            block_author = current_block.author
            if i < self.window_size:
                active_validators.add(current_qc.signatures.signers())
            if len(last_authors) < self.exclude_size:
                last_authors.add(block_author)
            current_qc = current_block.qc
            active_validators = active_validators\last_authors
            i = i + 1
        return active_validators.pick_one(seed = qc.vote_info.round)

    def update_leaders(self, qc):
        extended_route = qc.vote_info.parent_round
        qc_round = qc.vote_info.round
        current_round = PaceMaker.current_round
        if (extended_route + 1 == qc_round) and (qc_round + 1 == current_round):
            self.reputation_leaders[current_round + 1] = elect_reputation_leader(qc)


    def get_leader(self, round):
        if (round, leader) in self.reputation_leaders:
            return leader
        return self.validators[(round/2) % len(self.validators)]