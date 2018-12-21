"""
Return Fibonacci series
EG : 1,1,2,3,5,8.....
"""

n1 = 1
n2 = 1
l = [1]
for i in range(10):
    l.append(n2)
    n3 = n1+n2
    n1 = n2
    n2 = n3

print(l)
