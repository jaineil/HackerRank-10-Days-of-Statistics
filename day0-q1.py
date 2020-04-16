# Given an array, X of N integers 
# Calculate and print the respective Mean, Median and Mode 
# If your array contains more than one modal value..
# ..choose the numerically smallest one. 

import statistics as st
from collections import Counter

n = int(input())
nums = list(map(int, input().strip().split()))

print(st.mean(nums))
print(st.median(nums))

print(list(Counter(sorted(nums)).most_common()[0])[0])