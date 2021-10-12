from Ledger import *
from PaceMaker import *

validators = Validator.validators
window_size = f
exclude_size = f + 1
reputation_leaders = None


# def set_fields(vals, w_size, e_size, r_leaders):
#     global validators, window_size, exclude_size, reputation_leaders
#     validators = vals
#     window_size = w_size
#     exclude_size = e_size
#     reputation_leaders = r_leaders


def elect_reputation_leader(qc):
    print("In function: LeaderElection.elect_reputation_leader")
    global window_size, exclude_size
    active_validators = {}
    last_authors = {}
    current_qc = qc
    i = 0
    while i < window_size or len(last_authors) < exclude_size:
        current_block = Ledger.committed_block(current_qc.vote_info.parent_id)
        block_author = current_block.author
        if i < window_size:
            # signers is a set of validator ids
            active_validators.add(current_qc.signatures.signers())
        if len(last_authors) < exclude_size:
            # see safety validator id
            last_authors.add(block_author)
        current_qc = current_block.qc
        # backslash means complement set, make sure both are sets
        active_validators = active_validators - last_authors
        i += 1
    return active_validators.pick_one(seed=qc.vote_info.round)


def update_leaders(qc):
    print("In function: LeaderElection.update_leaders")
    global reputation_leaders
    extended_route = qc.vote_info.parent_round
    qc_round = qc.vote_info.round
    current_round = PaceMaker.current_round
    if (extended_route + 1 == qc_round) and (qc_round + 1 == current_round):
        reputation_leaders[current_round + 1] = elect_reputation_leader(qc)


def get_leader(round):
    global validators, reputation_leaders
    print("In function: LeaderElection.get_leader")
    if (round, leader) in reputation_leaders:
        return leader
    return validators[(round / 2) % len(validators)]
