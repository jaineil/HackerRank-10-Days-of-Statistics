# The ratio of boys to girls for babies born in Russia is 1.09:1 
# If there is  child born per birth... 
# What proportion of Russian families with...
# Exactly 6 children will have at least 3 boys?
# Answer is rounded to a scale of 3 decimal places
# Binomial Distribution - 1

import math

def binomialDist(x, n, p):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
    return(b)

b = 0
p = 1.09/2.09
n = 6

for i in range(3,7):
    b += binomialDist(i, n, p)   

print(round(b,3))