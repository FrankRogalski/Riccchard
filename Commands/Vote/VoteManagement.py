import re
import discord.message
from typing import List
from commands.vote.voting import Voting

votings = {}
keyword = "vote" #"|createvote\n|votefor\n|voteresults\n|delvote\nopenvotes"
helping = """|vote create <Topic> <option 1> <option 2> ... [option n] - Creation of a voting topic"
|vote vote <Topic> <option> - Vote for an option of a topic"
|vote result <Topic> - Get the outcomes of a Vote"
|vote del <Topic> - Delete a vote on a topic"
|vote votes - Shows all open votes"""

def use(message: discord.message) -> str:
    msg = message.content.split()[1:]

    output = ""
    if not msg:
        return 'Please specify an action, that should be performed'
    if msg[0] == "create":
        output = declare_vote(msg[1:])
    elif msg[0] == "vote":
        output = vote(msg[1:], str(message.author))
    elif msg[0] == "result":
        output = result(msg[1:])
    elif msg[0] == "del":
        output = delete_vote(msg[1:])
    elif msg[0] == "votes":
        output = get_votings()
    else:
        output = 'Thats not a valid option'
    return output

def declare_vote(votes: List[str]) -> str:
    if len(votes) < 3 or votes[0] in votings: return "Please specify a name and at least 2 voting Options"
    votings[votes[0]] = Voting(votes[0], votes[1:])
    return f"Wahl über: {votes[0]}\n" + "\n".join(i for i in set(votes[1:]))

def vote(vote: List[str], user: str) -> str:
    if len(vote) != 2 or not vote[0] in votings \
        and votings[vote[0]].vote(vote[1], user): # voting is taking place here
        return "This poll either doesn't exist or you already voted for it"
    return f"{user.split('#')[0]} has voted for {vote[2]}"

def result(votes: List[str]) -> str:
    return votings[votes[0]].get_result()

def delete(key: str) -> str:
    del votings[key]
    return key

def delete_vote(votes: List[str]) -> str:
    if len(votes) < 1: return "Please provide at least one vote that should be deleted"
    return f"The vote/s {' '.join(delete(vote) for vote in votes if vote in votings)} where deleted"

def get_votings() -> str:
    return f"Votes open at the moment: {''.join(votes for votes in votings.keys())}"
