"""12< =<65 member resident"""


def discount(age, ismember, isresident):
    if age>=65 or age<12 or ismember==True or isresident==True: 
        print("qualified")
    else:
        print("unqualified")
discount(12, False, False)


