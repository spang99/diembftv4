from Ledger import *
from PaceMaker import *

validators = None
window_size = None
exclude_size = None
reputation_leaders = None


def __init__(self, validators, window_size, exclude_size, reputation_leaders):
    self.validators = validators
    self.window_size = window_size
    self.exclude_size = exclude_size
    self.reputation_leaders = reputation_leaders


def elect_reputation_leader(qc):
    print("In function: LeaderElection.elect_reputation_leader")
    global window_size, exclude_size
    active_validators = {}
    last_authors = {}
    current_qc = qc
    i = 0
    while (i < window_size) or len(last_authors) < exclude_size:
        current_block = Ledger.committed_block(current_qc.vote_infor.parent_id)
        block_author = current_block.author
        if i < self.window_size:
            # signers is a set of ids?
            # set of validator ids
            active_validators.add(current_qc.signatures.signers())
        if len(last_authors) < exclude_size:
            # see safety validator id
            last_authors.add(block_author)
        current_qc = current_block.qc
        # backslash means complement set, make sure both are sets
        active_validators = active_validators - last_authors
        i = i + 1
    return active_validators.pick_one(seed=qc.vote_info.round)


def update_leaders(qc):
    print("In function: LeaderElection.update_leaders")
    extended_route = qc.vote_info.parent_round
    qc_round = qc.vote_info.round
    current_round = PaceMaker.current_round
    if (extended_route + 1 == qc_round) and (qc_round + 1 == current_round):
        self.reputation_leaders[current_round + 1] = elect_reputation_leader(qc)


def get_leader(round):
    global validators, reputation_leaders
    print("In function: LeaderElection.get_leader")
    if (round, leader) in reputation_leaders:
        return leader
    return validators[(round / 2) % len(validators)]
