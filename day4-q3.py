# The probability that a machine produces a defective product is 1/3 
# What is the probability that the 1st defect is found during the 5th inspection
# Geometric Distribution - 1

num , denom = map(int, input().split())
n = int(input())

p = num / denom
q = 1-p

print(round(((q**(n-1))*p),3))