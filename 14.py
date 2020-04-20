# This problem was asked by Google

# The area of a circle is defined as πr^2
# Estimate π to 3 decimal places using a Monte Carlo method

# Hint: The basic equation of a circle is x^2 + y^2 = r^2

from random import random

def estimate_PI_using_monte_carlo():
    # Let the center of both square and circle be at (0,0)
    # Let the side of square be 1unit, radius of inscribed circle = 0.5unit
    s, r = 1, 0.5
    n = 10000   
    circle_points = total_points = 0
    for i in range(n):
        x = random() - 0.5  # random point inside square ie [-0.5, 0.5]
        y = random() - 0.5
        if x**2 + y**2 <= r**2:
            circle_points += 1
        total_points += 1
    pi = 4.0 * circle_points / total_points
    return round(pi, 3)

print('Pi =', estimate_PI_using_monte_carlo())
