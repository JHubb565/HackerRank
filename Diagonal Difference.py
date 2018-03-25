# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#
# Input Format
#
# The first line contains a single integer,  denoting the number of rows and columns in the matrix .
# The next  lines denote the matrix 's rows, with each line containing  space-separated integers describing the columns.
#
# Constraints
#
# Output Format
#
# Print the absolute difference between the sums of the matrix's two diagonals as a single integer.
#
# Sample Input
#
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# Sample Output
#
# 15
# Explanation
#
# The primary diagonal is:
# 11
#    5
#      -12
# Sum across the primary diagonal: 11 + 5 - 12 = 4
#
# The secondary diagonal is:
#
#      4
#    5
# 10
# Sum across the secondary diagonal: 4 + 5 + 10 = 19
# Difference: |4 - 19| = 15
#
# Note: |x| is the absolute value of x

def diagnoldifference(n,matrix):
    list = []
    list2 = []
    length = len(matrix)
    for i in range(n):
       list.append(matrix[i][i])
    for i in range(n):
        list2.append(matrix[i][n-i-1])
    x = sum(list)
    y = sum(list2)
    z = abs(x - y)
    return z



n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().rstrip().split())))
print(matrix)
# print(len(matrix[0]))
result = print(diagnoldifference(n,matrix))

