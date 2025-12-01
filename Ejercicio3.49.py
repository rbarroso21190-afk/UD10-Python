"""Escriu un programa que, utlitzant, la sentència for mostri el següent:
	5 4 3 2 1
	4 3 2 1
	3 2 1
 	2 1
	1
"""

for a in range(5, 0, -1):     
    for b in range(a, 0, -1):  
        print(b, end=" ")
    print()