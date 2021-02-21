from team import Team
import numpy as np
import pandas as pd
import pdb

class Group:
    def __init__(self, teams):
        self.teams = teams
        if len(self.teams) % 2 == 1: self.teams = self.teams + [None]
        
    def pairing_tables(self):
        """ Construction of pairing tables by Richard Schurig 
            https://en.wikipedia.org/wiki/Round-robin_tournament#Original_construction_of_pairing_tables_by_Richard_schurig_(1886)  """
        n = len(self.teams)
        
        indices = list(range(n))
        half = n // 2

        rounds = [f'round {i+1}' for i in range(n-1)]
        games = [f'game {i+1}' for i in range(half)]
        
        schedule = pd.DataFrame(index=rounds, columns = games)
        
        for i in range(n-1):
            index_1 = indices[:half]
            index_2 = indices[half:]
            # index_2.reverse()
            # pdb.set_trace()

            for j in range(half):
                team_1 = self.teams[index_1[j]]
                team_2 = self.teams[index_2[j]]
                schedule.iloc[i, j] = [team_1, team_2]
            indices = indices[half:-1] + indices[:half] + indices[-1:]
        return schedule


if __name__ == "__main__":
    print("start")
    a = Team('a')
    b = Team('b')
    c = Team('c')
    d = Team('d')
    e = Team('e')

    rr = Group([a.name, b.name, c.name, d.name])
    
    print(rr.pairing_tables())
    # pdb.set_trace()
