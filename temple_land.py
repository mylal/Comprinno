# # Question 3: Temple Land

# Pseudo Code: -
# (1) take number of test case as input - t
# (2) for loop in range upto t-1, take length of the strips land and number of parts it has been divided as n and s respectively
# (3) initially take selected as yes
# (4) check if length of strip is divided by 2, selected wil be "no"
# (5) check if length of strip isnot divisible by 2 ,take a emptly list as test , for loop in range utp n//2 , append all the i value to the test ,
# (6) After that concatinate the test with the reversed test
# (7)Check if all the parts of strips land are in the test list which satisfies the condition of the valid strip
# (8) Output the strips is valid or not by printing yes or no

t = int(input())  # number of test cases
for i in range(t):  # for loop in range upto t-1
    n = int(input())  # length of the strips
    s = list(map(int, input().split()))  # number of parts it has been divided
    selected = "yes"  # Initially strip is selected
    if n % 2 == 0:  # check if length is divisible by 2
        selected = "no"  # strip not selected
    else:  # if n is not divisible by 2
        test = list()  # empty list
        for i in range(n//2 + 1):  # for loop in range n//2 (floor division)
            test.append(i+1)  # add i to the list each time
        test = test + test[:-1][::-1]  # test will be test + reversed test
        if s != test:  # check if all the parts lies within the test list
            selected = "no"  # strip not selected
    # strip is selected if it's value isnot manipulated by the above condition
    print(selected)
