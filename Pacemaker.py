from BlockTree import *
from Safety import *

current_round = 0
last_round = None
pending_timeouts = []
delta = None


def get_round_timer(r):
    print("In function: Pacemaker.get_round_timer")
    # need to figure out formula
    return 4 * delta


def start_timer(new_round):
    print("In function: Pacemaker.start_timer")
    global current_round
    stop_timer()
    current_round = new_round
    # start local timer for round current round for duration get round timer(current round)
    start_timer(current_round, get_round_timer(current_round))


def local_timeout_round():
    global current_round
    print("In function: Pacemaker.local_timeout_round")
    save_consensus_state()
    timeout_info = Safety.make_timeout(current_round, BlockTree.high_qc, last_round_tc)
    broadcast(TimeoutMsg(timeout_info, last_round_tc, BlockTree.high_commit_qc))


def process_remote_timeout(tmo):
    # tmo is a timeout message
    print("In function: Pacemaker.process_remote_timeout")
    global current_round
    tmo_info = tmo.tmo_info
    if tmo_info.round < current_round:
        return None
    if tmo_info.sender not in self.pending_timeouts[tmo_info.round].senders:
        # self.pending_timeouts[tmo_info.round] = self.pending_timeouts[tmo_info.round] union {tmo_info}
        # figure this out
        pass
    if self.pending_timeouts[tmo_info.round].senders == f + 1:
        stop_timer()
        self.local_timeout_round()
    if self.pending_timeouts[tmo_info.round].senders == 2 * f + 1:
        return TC(tmo_info.round, {t.high_qc.round | t in self.pending_timeouts[tmo_info.round]},
                  {t.signature | t in self.pending_timeouts[tmo_info.round]})
    return None


def stop_timer():
    print("In function: Pacemaker.stop_timer")

    pass


def advance_round_tc(tc):
    print("In function: Pacemaker.advance_round_tc")
    if tc is None or tc.round < self.current_round:
        return False
    last_round_tc = tc
    start_timer(tc.round + 1)
    return True


def save_consensus_state():
    print("In function: Pacemaker.save_consensus_state")
    pass


def advance_round_qc(self, qc):
    print("In function: Pacemaker.advance_round_qc")
    if qc.vote_info.round < self.current_round:
        return False
    last_round_qc = None
    self.start_timer(qc.vote_info.round + 1)
    return True
