import unittest
from Vector import *

class VectorTests(unittest.TestCase):
    def test_add(self):
        a = vector([1,2,3,4])
        b = vector([7,8,9,10])
        c = a+b
        assert(c[0] == 8 and c[1] == 10 and c[2] == 12 and c[3] == 14)
    
    def test_dot_simpe(self):
        a = vector([1,2,3,4])
        b = vector([7,8,9,10])
        assert(a.dot(b) == 50)
        
    def test_dot_orthogonal(self):
        a = vector([1,0,0,1])
        b = vector([0,1,0,1])
        assert(a.dot(b) == 0)
    
    def test_mul_number(self):
        a = vector([1,2,3,4])
        c = a*2
        assert(c[0] == 2 and c[1] == 4 and c[2] == 6 and c[3] == 8)
    
    def test_mul_matrix(self):
        m = matrix([[2,0,0,0],[0,2,0,0],[0,0,2,0],[0,0,0,1]])
        a = vector([1,2,3,4])
        c = m*a
        assert(c[0] == 2 and c[1] == 4 and c[2] == 6 and c[3] == 4)
    
if __name__ == '__main__':
    unittest.main()