# Question 11: Id and Ship

# Pseudo Code: -
# (1) Take number of test cases as input - n
# (2) For loop in range(n), take id and assign to 'a'
# (3) Check if 'a' euqal to 'b' or 'B', print "Battleship"
# (4) Check if 'a' euqal to 'c' or 'C', print "Cruiser"
# (5) Check if 'a' euqal to 'd' or 'D', print "Destroyer"
# (6) Check if 'a' euqal to 'f' or 'F', print "Frigate"

n = int(input())  # number of test cases
for i in range(n):  # for loop in range upto n-1
    a = input()  # take input
    if a == 'B' or a == 'b':  # for input 'b' or 'B' print "Battleship"
        print("BattleShip")
    elif a == 'C' or a == 'c':  # for input 'c' or 'C' print "Cruiser"
        print("Cruiser")
    elif a == 'D' or a == 'd':  # for input 'd' or 'D' print "Destroyer"
        print("Destroyer")
    elif a == 'F' or a == 'f':  # for input 'f' or 'F' print "Frigate"
        print("Frigate")
