#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    val = 0
    pairs = 0
    while val < n-1:
        print("My array", ar)
        print("Check for a pair on item: ", val)
        new = 0
        count = val+1
        while count < n:
            print("Current check: ", count)
            if ar[val] == ar[count]:
                print("Found a pair at spaces: ", val, " and ", count)
                print("Deleting ", ar[count])
                del(ar[val+count])
                print("Deleting ", ar[val])
                del(ar[val])
                pairs += 1
                print("Current pairs: ", pairs)
                n -= 2
                new = 1
                print ("Current n: ", n)
                break
            else:
                count += 1
        if new == 1:
            val = 0
        else:
            print("No pairs found")
            val += 1

    return pairs

#total = 10
#socks = [1,1,3,1,2,1,3,3,3,3]
total = 9
socks = [10,20,20,10,10,30,50,10,20]
testing = sockMerchant(total,socks)
print("Final value:", testing)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     ar = list(map(int, input().rstrip().split()))

#     result = sockMerchant(n, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()