import numpy as np
from scipy import norm

"""
Parameters:
    S    : Underlying asset price
    K    : Strike price
    T    : Time to expiration (years)
    r    : Risk-free interest rate
    sigma: volatility of the underlying asset
"""

def d1(S, K, T, r, sigma):
    if S <= 0:
        raise ValueError("Asset price must be positive.")
    if K <= 0:
        raise ValueError("Strike price must be positive.")
    if T <= 0:
        raise ValueError("Time must be positive.")
    if sigma <= 0:
        raise ValueError("Volatility must be positive")
    
    return (np.log(S/K) + (r + .5 * pow(sigma, 2)) * T) / (sigma * np.sqrt(T))
    


def d2(S, K, T, r, sigma):
    pass

def call_price(S, K, T, r, sigma):
    pass

def pull_price(S, K, T, r, sigma):
    pass



if __name__ == "__main__":
    pass
