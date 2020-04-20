# A random variable, X, follows Poisson distribution 
# With mean of 2.5 
# Find the probability with which the random variable X is equal to 5
# Poisson Distribution - 1

import math

lamda = 2.5
lamda_neg = -2.5
k = 5
e = 2.71828
res = ((lamda**k)*(e**lamda_neg))/math.factorial(k)
print(round(res,3))