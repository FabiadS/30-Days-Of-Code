# Objective
# Today, we're learning about Key-Value pair mappings using a Map or Dictionary data structure. 

# Task
# Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. 
#You will then be given an unknown number of names to query your phone book for. For each name queried, 
#print the associated entry from your phone book on a new line in the form name=phoneNumber; 
#if an entry for name is not found, print Not found instead.

# Note: Your phone book should be a Dictionary/Map/HashMap data structure.

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
dict_ = {}

for i in range(n):
    name, phone_number = input().split()
    dict_[name] = phone_number
    
while True:
    
    try:
        name = input()
    
        if(name in dict_):
            print(f'{name}={dict_[name]}')
        else:
            print("Not found")
    except:
        break