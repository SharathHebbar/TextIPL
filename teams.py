
def select_team(s):
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
    if(s < 11):
        print("You have selected {} team".format(d[s]))
    else:
        print("select a valid team number")
