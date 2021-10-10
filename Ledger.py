from Safety import *
from BlockTree import *
from collections import deque
import nacl.hash
import nacl.encoding

class Ledger:
    u = Safety.validator_id
    filename = "database" + str(u) + ".txt"
    f = open(filename, "w+")
    f.close()
    commits = {}
    q_size = 2*u
    commit_queue = deque() #stores the last q_size committed blocks
    ledger_info = 0
    printf("database for validator %d created", u)
    
    #We're not maintaining a separate pending tree in Ledger as mentioned in the phase 2 document
    #We're just executing txns on whatever exists in the file and returning the hash of file contents
    def speculate(prev_block_id, block_id, txns):
        print("In function: Ledger.speculate")
        if BlockTree.pending_block_tree.root is prev_block_id:
            self.ledger_info = nacl.hash.sha256([self.ledger_info, txns], encoder=nacl.encoding.HexEncoder)
        else:
            printf("Inconsistency in validator %d", self.u)

    def commit(block_id):
        print("In function: Ledger.commit")
        if block_id in BlockTree.pending_block_tree.blocks:
            bl = BlockTree.pending_block_tree.blocks[block_id]
            f = open(Ledger.filename, "a")
            f.append(bl.payload)
            f.close()
            self.commits[block_id] = bl
            self.deque.append(bl)
            printf("Committed block %d", block_id)
            if (len(commit_queue) > 10):
                self.commits.pop(commits[self.commit_queue[0]])
                self.commit_queue.pop_left()
            self.ledger_info = nacl.hash.sha256([bl.qc.ledger_commit_info, bl.payload], encoder=nacl.encoding.HexEncoder)
            return self.ledger_info

    def committed_block(block_id)
        return self.commits[block_id]
    
    def pending_state(block_id):
        return self.ledger_info