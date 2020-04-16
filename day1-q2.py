# The interquartile range of an array is 
# Difference between its first (Q1) and third (Q3) quartiles
# Given an array X ('data' in our case) of  n-integers 
# An array F ('freq' in our case) representing the respective frequencies of X's elements, 
# Construct a data set S, where each Xi occurs at frequency Fi 
# Then calculate and print S's interquartile range 
# Result should be rounded to a scale of 1 decimal place

import statistics as st

n = int(input())
data = list(map(int, input().strip().split()))
freq = list(map(int, input().strip().split()))

S = []
for i in range(n):
    S += [data[i]] * freq[i]
S.sort()
N = len(S)

if n%2 != 0:
    q1 = st.median(S[:N//2])
    q3 = st.median(S[N//2+1:])
else:
    q1 = st.median(S[:N//2])
    q3 = st.median(S[N//2:])

iqr = round(float(q3-q1), 1)
print(iqr)