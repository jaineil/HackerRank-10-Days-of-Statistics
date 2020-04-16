# Given an array X of n-integers 
# Calculate the respective 
# First quartile (Q1), second quartile (Q2), and third quartile (Q3) 
# It is guaranteed that Q1, Q2 and Q3 are integers.
from statistics import median

n = int(input())
X = sorted(map(int, input().strip().split()))

print(int(median(X[:n//2]))) #Q1
print(int(median(X))) #Q2
print(int(median(X[(n+1)//2:]))) #Q3