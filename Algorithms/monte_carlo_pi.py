import random as rn 
import math
"""
Proximating pi using the ratio of a queter of a unit circle and unit squere r=1
wich is approximate the probability of a point landing in the circle using 
monte carlo(a math technique used to predict the future value of an uncertain event)
"""
def monte_carlo_pi(num_samples=1_000_000):
        count = 0 # number of points inside the unit circle
        for _ in range(num_samples):
            x, y = rn.random(), rn.random() # random co-ordinates for each loop 
            if x**2 + y**2 <=1: # check if the point fall inside the circle
                count +=1 # sum(1 for _ in range(samples) if random.random()**2 + random.random()**2 <= 1)
        return (count / num_samples) * 4 # the ~proximation of pi given that the queter of a unit circle fits perfect inside the unit squere
        
print(f"pi ~ {monte_carlo_pi()}")
        