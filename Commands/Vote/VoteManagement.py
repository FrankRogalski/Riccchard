import re
from Commands.Vote.Voting import Voting

class VoteManagement:
    def __init__(self):
        self.__votings = {}

    def use (self, msg):
        mess = msg.content
        mess = ' '.join(mess.split())
        nachricht = mess.split(" ")

        output = ""
        if len(nachricht) <= 1:
            return 'Please specify an action, that should be performed'
        if nachricht[1] == "create":
            output = self.__declare_vote(nachricht[2:])
        elif nachricht[1] == "vote":
            output = self.__vote(nachricht[2:], str(msg.author))
        elif nachricht[1] == "result":
            output = self.__result(nachricht[2:])
        elif nachricht[1] == "del":
            output = self.__delete_vote(nachricht[2:])
        elif nachricht[1] == "votes":
            output = self.__get_votings()
        else:
            output = 'Thats not a valid option'
        return output, False

    def __declare_vote(self, votes):
        if len(votes) < 3 or votes[0] in self.__votings: return "Please specify a name and at least 2 voting Options"
        self.__votings[votes[0]] = Voting(votes[0], votes[1:])
        return f"Wahl über: {votes[0]}\n" + "\n".join(i for i in set(votes[1:]))

    def __vote(self, vote, user):
        if len(vote) != 2 or not vote[0] in self.__votings \
            and self.__votings[vote[0]].vote(vote[1], user): # voting is taking place here
            return "This poll either doesn't exist or you already voted for it"
        return f"{user.split('#')[0]} has voted for {vote[2]}"

    def __result(self, votes):
        return self.__votings[votes[0]].get_result()

    def __delete(self, key):
        del self.__votings[key]
        return f"{key}"

    def __delete_vote(self, votes):
        if len(votes) < 1: return "Please provide at least one vote that should be deleted"
        return f"The vote/s {' '.join(self.__delete(vote) for vote in votes if vote in self.__votings)} where deleted"

    def __get_votings(self):
        return f"Votes open at the moment: {''.join(votes for votes in self.__votings.keys())}"

    def get_keyword(self):
        return "vote" #"|createvote\n|votefor\n|voteresults\n|delvote\nopenvotes"

    def helping(self):
        return """|vote create <Topic> <option 1> <option 2> ... [option n] - Creation of a voting topic"
|vote vote <Topic> <option> - Vote for an option of a topic"
|vote result <Topic> - Get the outcomes of a Vote"
|vote del <Topic> - Delete a vote on a topic"
|vote votes - Shows all open votes"""
