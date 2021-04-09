""" This module counts the number of lines in a standard input 
Input: any string from the system

"""


import sys


count = 0

for line in sys.stdin:
    count += 1


print(count, "Lines in standard input")


