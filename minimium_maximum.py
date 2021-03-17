# Question 9: Minimum Maximum

# pseudo Code: -
# (1) Take number of test cases as input - N
# (2) for loop in range(N), take n and l as array length and elements inn integer form
# (3) Calculate m as minimium element by min(l)
# (4) Then the minimium cost required for transformation will be (n-1)*3

N = int(input())  # number of test cases
for _ in range(N):  # for loop in range upto N-1
    n = int(input())  # length of the array
    l = list(map(int, input().split()))  # list with elements in integer form
    m = min(l)  # find minimum value of the list
    print((n-1)*m)  # minimum cost required for transformtion
