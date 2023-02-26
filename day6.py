# Objective
# Today we will expand our knowledge of strings, combining it with what we have already learned about loops. 

# Task
# Given a string, S, of length N that is indexed from 9 to N-1,
# print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line 

# Note: 0 is considered to be an even index.

# Example
# s = adbecf

# Print abc def

# Enter your code here. Read input from STDIN. Print output to STDOUT

entrada = int(input().strip())

i = 0

while(i < entrada):
    palavra = input().strip()
    
    even = ""
    odd = ""
    
    for x in range(len(palavra)):
        if(x % 2 != 0):
            odd = odd + palavra[x]
        else:
            even = even + palavra[x]
    
    i = i + 1
    print(even, odd)
