# In a certain plant, the time taken to assemble a car is a random variable, X 
# It has a normal distribution with a mean of 20 hours 
# A standard deviation of 2 hours 
# What is the probability that a car can be assembled at this plant in: 
# Less than 19.5 hours?
# Between 20 and 22 hours?
# Normal Distribution - 1

import math
mean, sd = 20, 2
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (sd * (2 ** 0.5))))

# Less than 19.5
print('{:.3f}'.format(cdf(19.5)))
# Between 20 and 22
print('{:.3f}'.format(cdf(22) - cdf(20)))