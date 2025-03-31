"""
Program in Python to merge following dictionaries to create a new one:
	dic1={1:10, 2:20}
	dic2={3:30, 4:40}
	dic3={5:50, 6:60}

A program in python to merge the dictionary and display the resulting dictionary.
"""

dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50, 6:60}

dict4= dict1|dict2|dict3
print(dict4)

dict2.update(dict3)
dict1.update(dict2)
print(dict1)

