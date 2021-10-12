import time
from BlockTree import *
from Safety import *
from Validator import *

current_round = 0
last_round_tc = None
pending_timeouts = []
delta = None
# time_started = 0
# time_stopped = 0


def get_round_timer(r):
    print("In function: Pacemaker.get_round_timer")
    # need to figure out formula
    return 4 * delta


def start_timer(new_round):
    print("In function: Pacemaker.start_timer")
    global current_round, time_started
    stop_timer(current_round)
    current_round = new_round
    # start local timer for round current round for duration get round timer(current round)
    # time_started = time.perf_counter()


def local_timeout_round():
    global current_round
    print("In function: Pacemaker.local_timeout_round")
    save_consensus_state()
    timeout_info = Safety.make_timeout(current_round, BlockTree.high_qc, last_round_tc)
    broadcast(TimeoutMsg(timeout_info, last_round_tc, BlockTree.high_commit_qc))


def process_remote_timeout(tmo):
    # tmo is a timeout message
    print("In function: Pacemaker.process_remote_timeout")
    global current_round, pending_timeouts
    tmo_info = tmo.tmo_info
    if tmo_info.round < current_round:
        return None
    if tmo_info.sender not in pending_timeouts[tmo_info.round].senders:
        pending_timeouts[tmo_info.round] = pending_timeouts[tmo_info.round].add(tmo_info)
    if len(pending_timeouts[tmo_info.round].senders) == f + 1:
        stop_timer(current_round)
        local_timeout_round()
    if len(pending_timeouts[tmo_info.round].senders) == 2 * f + 1:
        high_qc_rounds = []
        for info in pending_timeouts[tmo_info.round]:
            high_qc_rounds.add(info.high_qc)
        signatures = []
        for info in pending_timeouts[tmo_info.round]:
            signatures.add(info.signature)
        return BlockTree.TC(tmo_info.round, high_qc_rounds, signatures)
    return None


def stop_timer(r):
    global time_stopped
    print("In function: Pacemaker.stop_timer")
    # time_stopped = time.perf_counter()


def advance_round_tc(tc):
    print("In function: Pacemaker.advance_round_tc")
    global current_round, last_round_tc
    if tc is None or tc.round < current_round:
        return False
    last_round_tc = tc
    start_timer(tc.round + 1)
    return True


def save_consensus_state():
    print("In function: Pacemaker.save_consensus_state")
    pass


def advance_round_qc(qc):
    global current_round, last_round_tc
    print("In function: Pacemaker.advance_round_qc")
    if qc.vote_info.round < current_round:
        return False
    last_round_tc = None
    return True


def broadcast(msg):
    print("In function: Pacemaker.broadcast")
    # send a timeoutMsg to all other validators
    for validator in LeaderElection.validators:
        send_message((TimeoutMsg, msg), validator)
