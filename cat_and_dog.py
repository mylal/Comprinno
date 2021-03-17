# Question 6: Cats and Dogs

# Pseudo Code  :-
# (1) Take number of test cases as input - n
# (2) For loop in range(n)
# (3) Assign cat, dog and legs respectively to c, d, l
# (4) Initially assign max = 4*(c+d) and min = 0
# (5) check if no. of cats are double than the no. of dogs, then min will be 4*(c-d) because a dog can carry 2 cats
# (6) If above condition not satisfied, min will be 4*d
# (7) Check if no. of legs lies between min and max, and it is divisible by 4, print "yes"
# (8) Otherwise print "np"

n = int(input())  # number of test cases
for i in range(n):  # for loop in range upto n-1
    # assigining value to cat , dog and legs respectively
    c, d, l = [int(x) for x in input().split()]
    max, min = 4*(c+d), 0  # assig initial value for min and max
    if c > 2*d:  # check if no. of cats is double than no. of dogs , a dog can carry 2 cats
        min = 4*(c-d)
    else:
        min = 4*d  # if cat number is doublee or less , they can be carried on back of dogs
    # check if l lies between min and max value and also it is divisible by 4
    if l <= max and l >= min and l % 4 == 0:
        print('yes')  # counted properly
    else:
        print('no')  # not counted properly
