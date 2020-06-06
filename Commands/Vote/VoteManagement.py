import re
from commands.vote.voting import Voting

votings = {}
keyword = "vote" #"|createvote\n|votefor\n|voteresults\n|delvote\nopenvotes"
helping = """|vote create <Topic> <option 1> <option 2> ... [option n] - Creation of a voting topic"
|vote vote <Topic> <option> - Vote for an option of a topic"
|vote result <Topic> - Get the outcomes of a Vote"
|vote del <Topic> - Delete a vote on a topic"
|vote votes - Shows all open votes"""

def use (msg):
    mess = msg.content
    mess = ' '.join(mess.split())
    nachricht = mess.split()

    output = ""
    if len(nachricht) <= 1:
        return 'Please specify an action, that should be performed'
    if nachricht[1] == "create":
        output = declare_vote(nachricht[2:])
    elif nachricht[1] == "vote":
        output = vote(nachricht[2:], str(msg.author))
    elif nachricht[1] == "result":
        output = result(nachricht[2:])
    elif nachricht[1] == "del":
        output = delete_vote(nachricht[2:])
    elif nachricht[1] == "votes":
        output = get_votings()
    else:
        output = 'Thats not a valid option'
    return output

def declare_vote(votes):
    if len(votes) < 3 or votes[0] in votings: return "Please specify a name and at least 2 voting Options"
    votings[votes[0]] = Voting(votes[0], votes[1:])
    return f"Wahl über: {votes[0]}\n" + "\n".join(i for i in set(votes[1:]))

def vote(vote, user):
    if len(vote) != 2 or not vote[0] in votings \
        and votings[vote[0]].vote(vote[1], user): # voting is taking place here
        return "This poll either doesn't exist or you already voted for it"
    return f"{user.split('#')[0]} has voted for {vote[2]}"

def result(votes):
    return votings[votes[0]].get_result()

def delete(key):
    del votings[key]
    return f"{key}"

def delete_vote(votes):
    if len(votes) < 1: return "Please provide at least one vote that should be deleted"
    return f"The vote/s {' '.join(delete(vote) for vote in votes if vote in votings)} where deleted"

def get_votings():
    return f"Votes open at the moment: {''.join(votes for votes in votings.keys())}"
