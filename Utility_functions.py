from numpy import matrix
from Vector import *
from math import *

def get_identity_matrix():
    return matrix([[float32(i==j) for i in range(0,4)] for j in range(0,4)])
    
def get_zero_vector():
    return vector([0.0,0.0,0.0,1.0])

    
def get_for_scale(i, j, vec):
    if i==j:
        return vec[i]
    else:
        return 0
def scale_matrix(vec):
    return matrix([[float32 ( get_for_scale(i,j,vec) ) for i in range(0,4)] for j in range(0,4)])
    
    
def z_rotation(angle):
    angle_radians = radians(angle)
    return matrix([[cos(angle_radians), sin(angle_radians), 0.0, 0.0], [- sin(angle_radians), cos(angle_radians), 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]])
    
def x_rotation(angle):
    angle_radians = radians(angle)
    return matrix([[1.0, 0.0, 0.0, 0.0], [0.0, cos(angle_radians), sin(angle_radians), 0.0], [0.0, - sin(angle_radians), cos(angle_radians), 0.0], [0.0, 0.0, 0.0, 1.0]])

def y_rotation(angle):
    angle_radians = radians(angle)
    return matrix([[cos(angle_radians), 0.0, - sin(angle_radians), 0.0], [0.0, 1.0, 0.0, 0.0], [sin(angle_radians), 0.0, cos(angle_radians), 0.0], [0.0, 0.0, 0.0, 1.0]])

        
def rotation_matrix(vec):
    #rotate_z = z_rotation(vec.z)
    return z_rotation(vec.z)