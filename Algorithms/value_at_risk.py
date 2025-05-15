import numpy as np
"""
Calculate the VaR at a given confidence level(e.g 95%) using the historical method for a portfolio
"""
def historical_var(returns, confidence_level=0.95):
    returns_sorted = sorted(returns) # sort the return 
    print(f"sorted returns: {returns_sorted}")
    index = int((1-confidence_level) * len(returns))
    return -returns_sorted[index]

sample_returns = np.random.normal(0, 1, 1000) #simulate the value from gaussian normal distribution with mean: 0 and standard deviation: 1 a thousand timese
print(f"VaR (95%) ~ {historical_var(sample_returns, 0.95)}")
    