"""
Create the classes needed to make the following code work as shown:

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()

Output
Mike Jones: 3 votes
Susan Dore: 4 votes
Kim Waters: 1 votes

Susan Dore won: 50.0% of votes
Don't worry about ties or whether votes should be singular.
"""

class Candidate:
    def __init__(self, name):
        self._name = name
        self._votes = 0

    def __iadd__(self, num):
        if not isinstance(num, int):
            return NotImplemented

        self._votes += num
        return self

class Election:
    def __init__(self, candidates):
        self._candidates = candidates

    def results(self):
        winner_name = None
        winner_votes = 0
        overall_votes = 0
        for candidate in self._candidates:
            print(f'{candidate._name}: {candidate._votes} votes')
            overall_votes += candidate._votes
            if candidate._votes > winner_votes:
                winner_name = candidate._name
                winner_votes = candidate._votes
        votes_percent = 100 * (winner_votes / overall_votes)
        print(f'{winner_name} won: {votes_percent} of votes')






mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()             
        
          