import numpy as np 
"""
Estimate the price of a european call option
"""
def monte_carlo_call_price(S, K, T, r, sigma, num_samples=1_000_000):
    Z = np.random.standard_normal(num_samples)
    ST = S * np.exp((r - 0.5 * sigma**2)*T + sigma * np.sqrt(T)*Z)
    payoff = np.maximum(ST - K, 0)
    return np.exp(-r * T) * np.mean(payoff)
    
# S=100, K=100, T=1, r=5%, σ=20%
print(f"estimated call ~ {monte_carlo_call_price(100, 100, 1, 0.05, 0.2)}")