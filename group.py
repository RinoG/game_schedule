from team import Team
import numpy as np
import pandas as pd
import pdb

class Group:
    def __init__(self, teams):
        self.teams = teams
        self.is_even = len(teams) % 2 == 0
        
    def get_schurig_tables(self):
        """ Construction of pairing tables by Richard Schurig 
            https://en.wikipedia.org/wiki/Round-robin_tournament#Original_construction_of_pairing_tables_by_Richard_Schurig_(1886)  """

        n = len(self.teams)
        rounds = n - 1 if self.is_even else n
        matches = int(np.ceil(n / 2))
        
        table_1 = np.zeros([rounds, matches]).astype(int)
        table_2 = np.zeros([rounds, matches]).astype(int)
        
        counter = 0
        round_counter = 0
        for r in range(rounds):
            for m in range(matches):

                table_1[r, m] = counter % rounds
                table_2[rounds - 1 - r, matches - 1 - m] = \
                    (counter - round_counter) % rounds
                counter += 1
            round_counter += 1
            
        return table_1, table_2

    def get_even_tables(self):
        """ Update first column when number of teams is even.
            Last team (n) is alternatingly substituted for the for the first match """
        
        table_1, table_2 = self.get_schurig_tables()

        n = len(table_1)
        for i in range(n):
            if i % 2 == 0:
                table_2[i, 0] = n
            else:
                table_1[i, 0] = n
        
        return table_1, table_2

    def get_odd_tables(self):
        """ Delete first column when number of team is odd. """
        
        table_1, table_2 = self.get_schurig_tables()

        table_1 = np.delete(table_1, 0, 1)
        table_2 = np.delete(table_2, 0, 1)
        
        return table_1, table_2
    
    def get_pairing_tables(self):
        """ Returns the pairing table from a team in form of a Pandas-Dataframe. """
        
        if self.is_even:
            table_1, table_2 = self.get_even_tables()
        else:
            table_1, table_2 = self.get_odd_tables()

        # generate DataFrame
        col = [f'match {i+1}' for i in range(table_1.shape[1])]
        idx = [f'round {i+1}' for i in range(table_1.shape[0])]
        table = pd.DataFrame(index=idx, columns=col)
    
        # merge both tables
        for r in range(table_1.shape[0]):
            for m in range(table_1.shape[1]):
                table.iloc[r, m] = self.teams[table_1[r, m]], self.teams[table_2[r, m]]

        return table


if __name__ == "__main__":
    
    rr = Group(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
    
    print(rr.get_pairing_tables())
    # pdb.set_trace()
