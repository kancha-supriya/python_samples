"""
Create two seperate list for for odd and even number
"""

even = [i for i in range(1, 11) if i % 2 == 0]
odd = [i for i in range(1, 10) if i % 2 != 0]
print(even, odd)
