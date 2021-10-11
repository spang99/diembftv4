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
    q_size = 4*u #no of committed blocks remembered
    commit_queue = deque() #stores the last q_size committed blocks
    state_id = {} #description below:
    #stores exec_state_id with index as block_id
    #stores hash of the exec_state_id of the previous block and transactions of the current block
    #commit_state_id can also be obtained from this by referring to the previous block ids
    #This is taken care of in the Safety Module when it asks for state_id to populate its LedgerCommitInfo.commit_state_id
    #Hence not dealt with here
    printf("database for validator %d created", u)
    
    #We're NOT maintaining a separate pending tree in Ledger as mentioned in the phase 2 document
    #We're just executing txns on whatever exists in the file and returning the hash of file contents
    def speculate(prev_block_id, block_id, txns):
        print("In function: Ledger.speculate")
        if BlockTree.pending_block_tree[1].root is prev_block_id:
            self.state_id[block_id] = nacl.hash.sha256([self.state_id[prev_block_id], txns],\
                    encoder=nacl.encoding.HexEncoder)
        else:
            printf("Inconsistency in validator %d", self.u)

    def commit(block_id):
        print("In function: Ledger.commit")
        #if block_id in BlockTree.pending_block_tree.blocks:
            bl = BlockTree.pending_block_tree[0].blocks[block_id]
            f = open(Ledger.filename, "a")
            f.append(bl.payload)
            f.close()
            self.commits[block_id] = bl
            self.deque.append(bl)
            printf("Committed block %d", block_id)
            if (len(commit_queue) > q_size):
                self.commits.pop(commits[self.commit_queue[0]])
                self.commit_queue.pop_left()
            return self.state_id

    def committed_block(block_id)
        return self.commits[block_id]
    
    def pending_state(block_id):
        return self.state_id[block_id]
