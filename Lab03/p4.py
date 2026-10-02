"""Write a Python program to construct the following pattern,
using a nested for loop.

*
**
***
****
*****
****
***
**
*

"""
n = 5

# Upper half: 1 to 5 stars
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Lower half: 4 down to 1 stars
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()