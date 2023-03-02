# Objective
# Today, we're working with binary numbers.

# Task
# Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting 
#the maximum number of consecutive 1's in n's binary representation. 
#When working with different bases, it is common to show the base as a subscript.

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    
    _list = []
    while(n > 0):
        remainder = n % 2
        n = n/2
        
        _list.append(int(remainder))
        
    count, output = 0,0
    for i in range(0,len(_list)):
        if _list[i] == 0:
            count = 0
        else:
            count +=1
            output = max(output, count)
            
    print(output)