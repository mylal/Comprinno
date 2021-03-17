# # Question 5: Beautiful Array

# Pseudo Code: -
# (1) Take number of tests as input - t
# (2) for loop in range(t) take number of elements as n and also take elements
# (3) store the elemnts as list of integers
# (4) take cnt as list of occurences of the elements
# (5)take c by subtracing sum of count from the element list length
# (6) Check if c greater than 1 , print "not a beautiful array"
# (7) Otherwise check if cnt[0] and c , print "not a beautiful array"
# (8) Check if cnt[0] > 1 and cnt[2] == 0 , print "not a beautiful array"
# (9) Otherwise print "beautiful array"


t = int(input())  # number of test cases
for _ in range(t):  # for loop in range upto t-1
    n = int(input())  # number of elements
    l = list(map(int, input().split()))  # adding to directly as integgers
    cnt = [l.count(-1), l.count(0), l.count(1)]  # check number of occurences
    c = len(l) - sum(cnt)  # subtract the sum of cnt from length of elements
    if c > 1:  # if c is greater than 1
        print("no")  # Not a beautiful array
    else:
        if c and cnt[0]:  # check if both are true or 1 and 1
            print("no")  # not a beautiful array
        elif (cnt[0] > 1 and cnt[2] == 0):  # chwck if cnt[0] > 1 and cnt[2] == 0
            print("no")  # not a beautiful array
        else:  # if above conditions are not satisfied print yes
            print("yes")  # beautiful array
