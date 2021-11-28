from teams import select_team
from schedule import schedule_list

print("Select a team of your preference")
team = int(
    input("1: RCB\n2: DC\n3: CSK\n4: KKR\n5: MI\n6: SRH\n7: RR\n8: PK\n9: PWI\n10: GL\n"))
select_team(team)

next = input("1: ScheduleList\n2:Play\n")
if(next == 1):
    schedule_list(next)
else:
    print("")
