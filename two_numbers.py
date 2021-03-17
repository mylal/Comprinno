# Question 8: Two Numbers

# Pseudo Code :-
# (1) Take number of test cases as input - t
# (2) For loop in range upto t-1, assign Alice's initial number , Bob's initial number and Number of turns as a,b and n respectively
# (3) Check if number of turns is divisible by 2 , if true then double the value of 'a' and 'b'
# (4) Otherwise if it isnot divisble by 2 , double the value of 'a' only
# (5) Find the maximum of a and b
# (6) Find the minimum of a and b
# (7) Output the integer division

t = int(input())  # number of test cases
for i in range(t):  # for a loop in range upto t-1
    # assign a,b,n value from the input given , a=Alice's initial number , b=Bob's initial number  , n = number of turns
    a, b, n = map(int, input().split())
    if(n % 2 == 0):  # check if number of turns is divisible by 2
        a = a*2  # double the 'a' value
        b = b*2  # double the 'b' value
    else:  # if number of turn isnot divisible by 2
        a = a*2  # double only 'a' value
    ma = max(a, b)  # find maximum of a and b
    mi = min(a, b)  # find minimium of a and b
    print(ma//mi)  # Output the integer division
