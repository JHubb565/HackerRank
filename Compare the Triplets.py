#!/bin/python3

import os
import sys

#
# Complete the solve function below.
#
# def solve(a0, a1, a2, b0, b1, b2):

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_score = b_score = 0

for i in range(len(a)):
    if a[i] > b[i]:
        a_score += 1
    elif a[i] < b[i]:
        b_score += 1
    else:
        pass

print(a_score, b_score)

    # print(alice)
    # print(bob)
    # print(sum(alice),sum(bob))









# if __name__ == '__main__':
#     f = open(os.environ['OUTPUT_PATH'], 'w')
#
#     a0A1A2 = input().split()
#
#     a0 = int(a0A1A2[0])
#
#     a1 = int(a0A1A2[1])
#
#     a2 = int(a0A1A2[2])
#
#     b0B1B2 = input().split()
#
#     b0 = int(b0B1B2[0])
#
#     b1 = int(b0B1B2[1])
#
#     b2 = int(b0B1B2[2])
#
#     result = solve(a0, a1, a2, b0, b1, b2)
#
#     f.write(' '.join(map(str, result)))
#     f.write('\n')
#
#     f.close()
