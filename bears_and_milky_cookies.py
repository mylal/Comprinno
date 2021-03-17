# Question 4: Bear and Milky Cookies

# Pseudo Code: -
# (1) Take number of tests as input - n
# (2) For loop in range(n) take minutes and order as input
# (3) Store the order as list after spliting the spaces
# (4) Check if last order is "cookie" then the instruction isnot followed and then print("NO")
# (5) Assign initial value of 'folowed' as True
# (6) For loop in range(mins), check if order[i] == "cookie" and order[i+1] not equal to milk, then again we print("NO") and reassign 'followed' = False
# (7) Break the order of execution in if block
# (8) Check again if 'followed' = True and then print("YES")

n = int(input())  # number of test cases
for _ in range(n):  # for loop in range upto n-1
    mins = int(input())  # minutes spent in kitchen
    order = input().split()  # order that he eats something
    if order[-1] == "cookie":  # check if last order is cookie
        print("NO")  # instruction not followed
    else:
        followed = True
        for i in range(mins):
            # check if milk isnot taken after cookies
            if order[i] == "cookie" and order[i + 1] != "milk":
                print("NO")  # instruction not followed
                followed = False
                break  # break the if block

        if followed == True:
            print("YES")  # instruction followed
