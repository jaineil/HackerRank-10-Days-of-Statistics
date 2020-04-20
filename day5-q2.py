# The manager of a industrial plant is planning to buy a machine of either type A or type B. 
# For each day’s operation:
# The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88 
# The daily cost of operating A is cost_A = 160 + 40X^2
# The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.15 
# The daily cost of operating B is cost_B = 128 + 40Y^2
# Assume that the repairs take a negligible amount of time 
# The machines are maintained nightly to ensure that they operate like new at the start of each day 
# Find and print the expected daily cost for each machine.
# Poisson Distribution - 2

avg_A = 0.88 
avg_B = 1.55

cost_A = 160 + 40*(avg_A + avg_A**2)
cost_B = 128 + 40*(avg_B + avg_B**2)

print(round(cost_A, 3))
print(round(cost_B, 3))