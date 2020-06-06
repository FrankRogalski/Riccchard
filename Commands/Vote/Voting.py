class Voting:
    def __init__(self, topic, votes):
        self.__votes = {}
        self.__topic = topic
        self.__voters = []
        for vote in votes:
            self.__votes[vote] = 0

    def vote(self, vote, user):
        if user not in self.__voters and vote in self.__votes:
            self.__votes[vote] += 1
            self.__voters.append(user)
            return True
        return False

    def get_result(self):
        
        return f"Poll results: {self.__topic}\n" + '\n'.join(f'{vote_names}: {votes}' for vote_names, votes in self.__votes.items())
