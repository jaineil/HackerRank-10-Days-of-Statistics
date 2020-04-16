# Given an array X of N integers  
# And an array W representing the respective weights of X's elements 
# Calculate and print the weighted mean of X's elements 
# Answer should be rounded to a scale of 1 decimal place


N = int(input())
X = list(map(int, input().strip().split()))
W = list(map(int, input().strip().split()))

numerator = []
denominator = sum(W)

for i in range(N):
    z = X[i] * W[i]
    numerator.append(z)

numerator = sum(numerator)

res = round((numerator/denominator),1)

print(res)