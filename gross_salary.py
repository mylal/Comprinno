# Question 10: Gross Salary

# Pseudo Code :-
# (1) take number of test cases as input - t
# (2) For loop in range upto t-1 , take n as Basic Salary
# (3) Check if Basic Salary is greater than or equal to 1500 , in that case hra = 500 and da is 98% of basic salary
# (4) calculate gross salary as n*da*hra
# (5) check if basic salary is less than 1500 , hra = 10% of basic salary and da = 90% of basic salary
# (6) Again calculate gross salary as the step - 4
# (7) Output the gross salary

t = int(input())  # number of test cases
for i in range(t):  # for loop in range upto t - 1
    n = int(input())  # take n as Basic Salary
    if n >= 1500:  # check if basic salary is  greater than or equal to 1500
        hra = 500  # House Rent ALlowance as 500
        da = 0.98*n  # DearnessAllowance as 98% of Basic Salary
        c = n+da+hra  # calculate gross salary
    else:  # if basic salary less than 1500
        hra = 0.1*n  # House Rent Allowance as 10% of Basic Salary
        da = 0.9*n  # Dearness Allowance as 90% of Basic Salary
        c = n+da+hra  # calculate gross salary
    print(c)  # print gross salary
