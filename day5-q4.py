# The final grades for a Physics exam taken by a large group of students have a mean of 70
# A standard deviation of 10 
# If we can approximate the distribution of these grades by a normal distribution 
# What percentage of the students:
# Scored higher than 80 (grade > 80)
# Passed the test (grade >= 60)
# Failed the test (grade < 60)
# Normal Distribution - 2

import math
mean, std = 70, 10
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

print(round((1-cdf(80))*100,2))
print(round((1-cdf(60))*100,2))
print(round((cdf(60))*100,2))