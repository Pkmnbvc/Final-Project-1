class Candidate:
    def __init__(self, name: str):
        """
        Initializes a Candidate with a name and vote count.
        :param name:
        """
        self.name = name
        self.votes = 0

    def add_vote(self) -> None:
        """Increases the vote cound by 1."""
        self.votes += 1

    def __str__(self) -> str:
        return f"{self.name} - {self.votes} votes"

class VotingSystem:
    def __init__(self):
        """
        Initializes the voting system with predefined candidates.
        """
        self.candidates = {
            "1": Candidate("John"),
            "2": Candidate("Jane"),
        }
        self.total_votes = 0
    def vote(self, candidate_id: str) -> str:
        """
        Records a vote for the given candidate ID.
        :param candidate_id:
        :return:
        """
        if candidate_id in self.candidates:
            self.candidates[candidate_id].add_vote()
            self.total_votes +=1
            return f"Voted for {self.candidates[candidate_id].name}"
        else:
            raise ValueError("Invalid candidate ID")
    def get_results(self) -> str:
        """
        Returns a summary of the voting results
        :return:
        """
        results = "\n".join(str(candidate) for candidate in self.candidates.values())
        return f"Results:\n{results}\nTotal Votes: {self.total_votes}"
