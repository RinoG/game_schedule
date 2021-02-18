class Team:
    def __init__(self, name):
        self.name = name

    def test(self):        
        print(self.name)


if __name__ == "__main__":
    c = RoundRobin('hans')
    c.test()
