from team import Team
import numpy as np

class Group:
    def __init__(self, teams):
        self.teams = teams

    def roundrobin(self):
        
        for team in self.teams:
            team2 = np.roll(team)
            print(team)


if __name__ == "__main__":
    print("start")
    a = Team('a')
    b = Team('b')
    c = Team('c')
    d = Team('d')

    rr = RoundRobin([a.name, b.name, c.name, d.name])
    
    rr.test()
