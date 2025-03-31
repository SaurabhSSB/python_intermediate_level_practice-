"""
P to reverse map the dictionary items. Take dictionary as input from the user.

	For eg., Input: d = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
            Output: d = {65: 'A', 66: 'B', 67: 'C', 68: 'D'}

A program that traverses a given dictionary and reverses it.
"""

d: dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
d_2: dict = {}

for i in d:
    d_2[d[i]]= i

print(d_2)