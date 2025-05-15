import numpy as np 
"""
Compute the covariance matrix given matrix of asset return (rows=time, cols=asserts)
"""
def covariance_matrix(return_matrix):
    return np.cov(return_matrix, rowvar=False)

data = np.random.normal(0, 1, (100, 4)) # 100 time points, 4 assets
print(data)
print(f"covariance matrix ~ {covariance_matrix(data)}")

