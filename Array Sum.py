#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(n,ar):

    if n == len(ar):
        print("The sum is: ",sum(ar))
    else:
        print("The length of array was not specified correctly")

simpleArraySum(5,[1,2,3,4,5])