# A large elevator can transport a maximum of 9800 pounds 
# Suppose a load of cargo containing 49 boxes must be transported via the elevator 
# The box weight of this type of cargo follows a distribution with a mean of 205 pounds 
# A standard deviation of 15 pounds 
# Based on this information.. 
# What is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?
# Central Limit Theorem - 1

import math

x = int(input())
n = int(input())
mu = int(input()) # mean
sigma = int(input()) # standard deviation

mu_sum = n * mu 
sigma_sum = math.sqrt(n) * sigma

def cdf(x, mu, sigma):
    Z = (x - mu)/sigma
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(cdf(x, mu_sum, sigma_sum), 4))