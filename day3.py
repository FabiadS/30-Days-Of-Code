# Objective
# In this challenge, we learn about conditional statements. 

# Task
# Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# Complete the stub code provided in your editor to print whether or not n is weird.

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())
    
    if(N % 2 != 0):
        print("Weird")
    else:
        if (N >= 2 and N <= 5):
            print("Not Weird")
        elif (N >= 6 and N <= 20):
            print("Weird")
        else:
            print("Not Weird")