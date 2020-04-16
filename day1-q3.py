# Given an array X, of  N-integers 
# Calculate and print the Standard Deviation 
# Answer should be in decimal form, rounded to a scale of 1 decimal place

N = int(input())
X = list(map(int, input().strip().split()))

mean = sum(X) / N
variance = sum([((x - mean) ** 2) for x in X]) / N
sd = variance ** 0.5

print(round(sd,1))
