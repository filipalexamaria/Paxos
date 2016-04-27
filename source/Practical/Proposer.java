package filipalexamaria.paxos.practical;

import filipalexamaria.paxos.essential.EssentialProposer;
import filipalexamaria.paxos.essential.ProposalID;

public interface PracticalProposer extends EssentialProposer {

	public abstract void prepare(boolean incrementProposalNumber);

	public abstract void observeProposal(String fromUID, ProposalID proposalID);

	public abstract void receivePrepareNACK(String proposerUID,
			ProposalID proposalID, ProposalID promisedID);

	public abstract void receiveAcceptNACK(String proposerUID,
			ProposalID proposalID, ProposalID promisedID);

	public abstract void resendAccept();

	public abstract boolean isLeader();

	public abstract void setLeader(boolean leader);

	public abstract boolean isActive();

	public abstract void setActive(boolean active);

}
