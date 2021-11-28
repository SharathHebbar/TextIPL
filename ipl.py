
from random import *


class IPL():
    def __init__(self):
        d = {
            1: 'RCB',
            2: 'DC',
            3: 'CSK',
            4: 'KKR',
            5: 'MI',
            6: 'SRH',
            7: 'RR',
            8: 'PK',
            9: 'PWI',
            10: 'GL'
        }
        toss = 0
        self.toss = toss
        inn = 1
        self.inn = inn
        self.d = d
        z = 0
        self.z = z
        score = [0, 0]
        self.score = score
        wickets = 10
        self.wickets = wickets
        over = 0
        self.over = over
        if self.inn > 2:
            self.inn = 1
        if self.over > 19 or self.wickets == 10:
            self.over = 0
            self.wickets = 10
            self.score = [0, 0]

    def select_team(self, s):
        self.s = s
        if(s > 10):
            print("Select a valid team")
        else:
            print("You have selected {} team".format(self.d[s]))

    def schedule(self):
        print(
            "------------------ The scheduled matches for {} are: -----------------".format(self.d[self.s]))
        for i in self.d:
            if i != self.s:
                print('{} vs {} '.format(self.d[self.s], self.d[i]))

    def matches(self):
        if(self.z+1 != self.s):
            self.z += 1
        else:
            self.z += 2
        print("---------- The match is between {} vs {} ----------".format(
            self.d[self.s], self.d[self.z]))

    def scorecard(self):
        if self.over < 1:
            print("After 1 over the score is")
        else:
            print("After {} overs the score is".format(self.over))
        print("{}-{}".format(self.score[0], self.score[1]))

    def toss_call(self):
        print("Toss time")
        side = randint(0, 1)

        if side == 0:
            print("{} is tossing the coin {}".format(
                self.d[self.s], self.d[self.z]))

        elif side == 1:
            print("{} is tossing the coin {}".format(
                self.d[self.z], self.d[self.s]))
        call = int(input("1: Heads\n2: Tails\n"))
        t = randint(0, 1)
        if (call == 1 and t == 0) or (call == 2 and t == 1):
            if side == 0:
                self.toss = self.z
            elif side == 1:
                self.toss = self.s

        else:
            if side == 0:
                self.toss = self.s
            elif side == 1:
                self.toss = self.z
        print("Toss won by {} and choose Batting".format(self.d[self.toss]))

    def overs(self):
        if self.inn == 1:
            print("{} is batting ".format(self.d[self.toss]))
        elif self.inn == 2:
            if self.toss == self.s:
                print("{} is batting ".format(self.d[self.z]))
            else:
                print("{} is batting ".format(self.d[self.s]))
        if self.over == 19 or self.wickets == 0:
            print("Innings Over")
            self.inn += 1
            return
        for i in range(1, 7):
            if self.over == 19 or self.wickets == 0 or self.score[1] == 10:
                print("Innings Over")
                self.inn += 1
                return
            print("Ball {}.{} bowled".format(self.over, i))
            prob = randint(1, 2)
            if prob == 1:
                run = randint(0, 6)
                if run == 5:
                    run = run-1
                if run <= 1:
                    print("Batsman scored {} run".format(run))
                else:
                    print("Batsman scored {} runs".format(run))
                self.score[0] += run
            else:
                print("Bowler took the wicket")
                self.wickets -= 1
                self.score[1] += 1
        self.over += 1
        self.scorecard()


player_1 = IPL()
print("Select a team of your preference")
team = int(
    input("1: RCB\n2: DC\n3: CSK\n4: KKR\n5: MI\n6: SRH\n7: RR\n8: PK\n9: PWI\n10: GL\n"))
player_1.select_team(team)
player_1.schedule()
player_1.matches()

player_1.toss_call()
for i in range(0, 20):
    player_1.overs()
