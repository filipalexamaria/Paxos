
 +import time
 +
 +from paxos import basic
 +
 +class Proposer (basic.Proposer):
 +    '''
 +    This class augments the basic Paxos Proposer to provide a reasonable
 +    assurance of progress through a heartbeat mechanism used to detect leader
 +    failure and initiate leadership acquisition.
 +
 +    If one or more heartbeat messages are not received within the
 +    'liveness_window', leadership acquisition will be attempted by sending out
 +    phase 1a, Prepare messages. If a quorum of replies acknowledging leadership
 +    is received, the node has successfully gained leadership and will begin
 +    sending out heartbeat messages itself. If a quorum is not received, the
 +    node will continually resend its proposal every 'liveness_window' until either
 +    a quorum is established or a heartbeat with a proposal number greater than
 +    its own is seen.
 +
 +    Leadership loss is detected by way of receiving a heartbeat message from a proposer
 +    with a higher proposal number (which must be obtained through a successful phase 1).
 +
 +    This process does not modify the basic Paxos algorithm in any way, it merely seeks
 +    to ensure recovery from failures in leadership. Consequently, the basic Paxos
 +    safety mechanisms remain intact.
 +    '''
 +
 +    hb_period       = 1000
 +    liveness_window = 5000
 +
 +    timestamp       = time.time
 +
 +    #------------------------------
 +    # Subclass API
 +    #
 +    def send_prepare(self, node_uid, proposal_num):
 +        raise NotImplementedError
 +
 +    def send_accept(self, node_uid, proposal_num, proposal_value):
 +        raise NotImplementedError
 +
 +    def send_heartbeat(self, node_uid, leader_proposal_number):
 +        raise NotImplementedError
 +
 +    def schedule(self, msec_delay, func_obj):
 +        raise NotImplementedError
 +
 +    def on_leadership_acquired(self):
 +        pass
 +
 +    def on_leadership_lost(self):
 +        pass
 def __init__(self, my_uid, quorum_size, proposed_value=None, leader_uid=None,
 +                 hb_period=None, liveness_window=None):
 +        super(Proposer, self).__init__(quorum_size, proposed_value)
 +        self.my_uid       = my_uid
 +        self.leader_uid   = leader_uid
 +        self.leader_pnum  = None
 +        self._tlast       = self.timestamp()
 +        self._acquiring   = None # holds proposal number for our leadership request
 +
 +        if hb_period:       self.hb_period       = hb_period
 +        if liveness_window: self.liveness_window = liveness_window
 +        
 +
 +        
 +    def leader_is_alive(self):
 +        return self.timestamp() - self._tlast <= self.liveness_window
