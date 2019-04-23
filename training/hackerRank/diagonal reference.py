#!/bin/python3

n = 3
arr= [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

# Complete the diagonalDifference function below.
def diagonalDifference(a):
    # Complete this function  
    sum1  = 0
    sum2  = 0
    for i in range(n):
        sum1 += int(a[i][i])
        sum2 += int(a[i][n-i-1])
    return abs(sum1 - sum2)

print(diagonalDifference(arr))
