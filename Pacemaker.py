class Pacemaker:
    def __init__(self):
        self.current_round = 0
        self.last_round = None
        self.pending_timeouts = []

    def get_round_timer(r):
        # need to figure out formula
        return r


    def start_timer(self, new_round):
        self.stop_timer(self.current_round)
        self.current_round = new_round
        # start local timer for round current round for duration get round timer(current round)


    def local_timeout_round(self):
        save_consensus_state()
        time_info = Safety.make_timeout(self.current_round, Block_Tree.high_qc,last_round_tc)
        broadcast(TimeoutMsg(timeout_info, last_round_tc, Block_Tree.high_commit_qc))


    def process_remote_timeout(self, tmo):
        tmo_info = tmo.tmo_info
        if tmo_info.round < self.current_round:
            return None
        if tmo_info.sender not in self.pending_timeouts[tmo_info.round].senders:
            self.pending_timeouts[tmo_info.round] = self.pending_timeouts[tmo_info.round] union {tmo_info}
        if self.pending_timeouts[tmo_info.round].senders == f + 1:
            stop_timer(self.current_round)
            self.local_timeout_round()
        if self.pending_timeouts[tmo_info.round].senders == 2f + 1:
            return TC(tmo_info.round, {t.high_qc.round | t in self.pending_timeouts[tmo_info.round]}, {t.signature | t in self.pending_timeouts[tmo_info.round]})
        return None

    def stop_timer(self, current_round):
        pass


def advance_round_tc(self, tc):
       if tc is None or tc.round < self.current_round:
           return False
       last_round_tc = tc
       self.start_timer(tc.round + 1)
       return True


    def advance_round_qc(self, qc):
        if qc.vote_info.round < self.current_round:
            return False
        last_round_qc = None
        self.start_timer(qc.vote_info.round + 1)
        return True

