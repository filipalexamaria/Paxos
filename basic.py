The intent of this module is to provide a minimally correct implementation of
 the Paxos algorithm. These classes may be used as-is to provide correctness to
 more advanced implementations that enhance the basic model with such things as
 timeouts, retransmit, liveness-detectors, etc. 
 
 Instances of these classes are intended for a single instance of the algorithm
 only.
 '''
 
 class Proposer (object):
 
    def __init__(self, quorum_size, proposed_value=None):
         self.proposal_number      = None
         self.next_proposal_number = 1
        self.accepted_number      = None
         self.replied              = set()
        self.value                = proposed_value
         self.quorum_size          = quorum_size
 
         self.leader               = False
 
 
     def set_proposal(self, value):
