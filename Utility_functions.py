from numpy import matrix
from Vector import *

def get_identity_matrix():
    return matrix([[float32(i==j) for i in range(0,4)] for j in range(0,4)])
    
def get_zero_vector():
    return vector([0.0,0.0,0.0,1.0])
