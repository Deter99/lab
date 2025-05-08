import numpy as np

def union(A,B):
    return np.maximum(A,B)
def intersection(A,B):
    return np.minimum(A,B)
def complement(A):
    return 1-A
def difference(A,B):
    return np.maximum(A-B, 0)
def cartesian_product(A,B):
    return np.outer(A,B)
def max_min_composition(R1,R2):
    return np.maximum(np.minimum(R1,R2), 0)

A = np.array([0.2,0.7,0.8,0.4])
B = np.array([0.9,0.3,0.2,0.5])

R1 = cartesian_product(A,B)
R2 = cartesian_product(B,A)

print("Union = ", union(A,B))
print("Intersection = ", intersection(A,B))
print("Complement A = ", complement(A))
print("Complement B = ", complement(B))
print("Difference A-B = ", difference(A,B))
print("R1 =",R1)
print("R2 =",R2)
print("max_min_composition =", max_min_composition(R1,R2))


