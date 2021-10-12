from Ledger import *
from Safety import *


class Block:
    def __init__(self, author, round, payload, qc, id):
        self.author = author
        self.round = round
        self.payload = payload
        self.qc = qc
        self.id = id
        printf('Created new Block class')


class PendingBlockTree:
    def __init__(b):
        self.root = b.qc.vote_info.parent_id
        self.blocks = {}  # maps a block_id to a block
        self.blocks[b.id] = b
        printf('Created new PendingBlockTree class object')


class PendingBlockTreeQueue:
    def __init__():
        self.tree = deque()
        print("PendingBlockTreeQueue object created")

    def add(b):
        print('In function PendingBlockTreeQueue.add(); Adding new block to PendingBlockTreeQueue class')
        t = PendingBlockTree(b)
        self.tree.append(t)

    def prune(root):
        print('In function PendingBlockTreeQueue.prune()')
        if self.tree[0].root is root:
            printf('Pruning Block %d PendingBlockTreeQueue class', root)
            tree.popleft()
        else:
            print("Could not prune: INCONSISTENT STATE")


class LedgerCommitInfo:
    def __init__(self, commit_state_id, vote_info_hash):
        self.commit_state_id = id
        self.vote_info_hash = vote_info_hash
        printf('Created new LedgerCommitInfo class')


class ProposalMsg:
    def __init__(self, block, last_round_tc, high_commit_qc):
        self.block = block
        self.last_round_tc = last_round_tc
        self.high_commit_qc = high_commit_qc
        self.signature = Safety.signing_key.sign(block.id)  # signing_key expected in Safety module
        printf('Created new ProposalMsg class')


class QC:
    def __init__(self, vote_info, ledger_commit_info, signatures, sender):
        self.vote_info = vote_info
        self.ledger_commit_info = ledger_commit_info
        self.high_commit_qc = high_commit_qc
        self.signatures = signatures
        self.author = sender
        self.author_signature = Safety.signing_key.sign(signatures)  # signing_key expected in Safety module
        printf('Created new QC class')


class TimeoutMsg:
    def __init__(self, tmo_info, last_round_tc, high_commit_info):
        self.tmo_info = tmo_info
        self.last_round_tc = last_round_tc
        self.high_commit_info = high_commit_info
        print('Created new TimeoutMsg class')


class TC:
    def __init__(self, round, tmo_high_qc_rounds, tmo_signatures):
        self.round = round
        self.tmo_high_qc_rounds = tmo_high_qc_rounds
        self.tmo_signatures = tmo_signatures
        printf('Created new TC class')


class TimeoutInfo:
    def __init__(self, round, high_qc, sender):
        self.round = round
        self.high_qc = high_qc
        self.sender = sender
        self.signature = Safety.signing_key.sign(high_qc.round)  # signing_key expected in Safety module
        printf('Created new TimeoutInfo class')


class VoteInfo:
    def __init__(self, id, round, parent_id, parent_round, exec_state_id):
        self.id = id
        self.round = round
        self.parent_id = parent_id
        self.parent_round = parent_round
        self.exec_state_id = exec_state_id
        printf('Created new VoteInfo class')


class VoteMsg:
    def __init__(self, vote_info, ledger_commit_info, high_commit_qc, sender):
        self.vote_info = vote_info
        self.ledger_commit_info = ledger_commit_info
        self.high_commit_qc = high_commit_qc
        self.sender = sender
        self.signature = Safety.signing_key.sign(ledger_commit_info)  # signing_key expected in Safety module
        printf('Created new VoteMsg class')


class BlockTree:
    high_commit_qc = None
    high_qc = None
    pending_block_tree = PendingBlockTreeQueue()
    pending_votes = {}  # Declaring as dictionary for quick search
    vote_idx = None
    f = None

    def process_qc(qc):
        print('In function: process_qc')
        if (qc.ledger_commit_info.commit_state_id is not None) and (qc.vote_info.parent_id not in Ledger.commits):
            # included additional check to prevent committing an already committed block
            Ledger.commit(qc.vote_info.parent_id)
            self.pending_block_tree.prune(qc.vote_info.parent_id)  # replace prune
            if qc.vote_info.round > self.high_commit_qc.vote_info.round:
                self.high_commit_qc = qc
        if qc.vote_info.round > BlockTree.high_qc.vote_info.round:
            self.high_qc = qc

    # sequence of the following function has been changed as we are not maintaining any speculate tree in Ledger
    def execute_and_insert(b):
        print('In function: execute_and_insert')
        BlockTree.pending_block_tree.add(t)
        Ledger.speculate(b.qc.block_id, b.id, b.payload)

    def verify_signature(v):
        verify_key = Safety.get_verify_key(v.sender)
        try:
            verify_key.verify(v.signature)
        except:
            print('Incorrect Signature')
            return False
        return True

    def process_vote(v):  # v is of type VoteMsg
        print('In function: process_vote')
        process_qc(v.high_commit_qc)
        if verify_signature(v) is True:  # implement code for signature verification
            self.pending_votes[vote_idx].append([v.sender, v.signature])
            if len(BlockTree.pending_votes[vote_idx]) == 2 * f + 1:
                qc = QC(v.vote_info, v.ledger_commit_info, BlockTree.pending_votes[vote_idx], \
                        Safety.validator_id)
                print('Created quorum certificate')
                return qc
        return None

    def generate_block(txns, current_round):
        print('In function: generate_block')
        b = Block(Safety.validator_id, current_round, txns, high_commit_qc, nacl.hash.sha256 \
            ([Safety.validator_id, current_round, high_commit_qc.vote_info_id, \
              high_commit_qc.signatures]))
        # qc replaced by high_commit_qc
        return b
