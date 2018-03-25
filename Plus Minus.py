# Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.
#
# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.
#
# Input Format
#
# The first line contains an integer, , denoting the size of the array.
# The second line contains  space-separated integers describing an array of numbers .
#
# Output Format
#
# You must print the following  lines:
#
# A decimal representing of the fraction of positive numbers in the array compared to its size.
# A decimal representing of the fraction of negative numbers in the array compared to its size.
# A decimal representing of the fraction of zeros in the array compared to its size.
# Sample Input
#
# 6
# -4 3 -9 0 4 1
# Sample Output
#
# 0.500000
# 0.333333
# 0.166667
# Explanation
#
# There are  positive numbers,  negative numbers, and  zero in the array.
# The proportions of occurrence are positive: , negative:  and zeros:


def plusMinus(n,arr):
    Positive =[]
    Negative =[]
    Zero = []
    for i in arr:
        if i > 0:
            Positive.append(i)
        elif i < 0:
            Negative.append(i)
        elif i == 0:
            Zero.append(i)
    positive_fraction = (len(Positive)/n)
    negative_fraction = (len(Negative)/n)
    Zero_fraction = (len(Zero)/n)
    # print fraction values
    print((positive_fraction))
    print((negative_fraction))
    print((Zero_fraction))

# N = Array length
n = int(input())
arr = list(map(int, input().rstrip().split()))
plusMinus(n,arr)

