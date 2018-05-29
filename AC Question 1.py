import numpy as np
#
# n = 5
# m = [[5.,5.,5.,5.,5.]
#     ,[5.,1.,5.,5.,5.]
#     ,[5.,5.,5.,4.,5.]
#     ,[5.,5.,4.,2.,3.]
#     ,[0.,5.,5.,3.,4.]]
#
# list = []
# for row in m:
#     find_min = row
#     minimum = min(find_min)
#     list.append(minimum)
#
# print(sorted(list)[0:3])

# Complete the function below.

import sys
import os

def  find_minima(n, m):

    # LOOP THROUGH ROWS AND FIND MINIMUM
    list = []
    for row in m:
        # get row
        current_row = row
        # find minimum
        minimum = min(current_row)
        # append minimum to list
        list.append(minimum)
    # return sorted output - 3
    print(sorted(list)[0:3])


# f = open(os.environ['OUTPUT_PATH'], 'w')
# _n = int(input());
#
# _m_rows = 0
# _m_cols = 0
# _m_rows = int(input())
# _m_cols = int(input())
#
# _m = []
# for _m_i in range(_m_rows):
#     _m_temp = [float(_m_t) for _m_t in input().strip().split(' ')]
#     _m.append(_m_temp)
#
# res = find_minima(_n, _m)
# for res_cur in res:
#     f.write(str(res_cur) + "\n")

# f.close()