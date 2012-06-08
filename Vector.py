from numpy import *

class vector(ndarray):
    def __new__(cls, *args, **kwargs):
        return ndarray.__new__(cls, [4,1])
    
    def __init__(self, *args, **kwargs):
        if len(args) != 1:
            raise TypeError("Required one dimension")
        if len(args[0]) != 4:
            raise TypeError("Required 4 coordinates")
        for pos,val in enumerate(args[0]):
            ndarray.__getitem__(self,pos).__setitem__(0,val)
    
    
    def __array_finalize__(self, obj):
        pass
        
    def __getitem__(self, pos):
        return ndarray.__getitem__(ndarray.__getitem__(self,pos), 0)
        
    def __setitem__(self, pos, val):
        ndarray.__setitem__(self, 0, val)
    
    def __repr__(self):
        return ""+str(self[0])+" "+str(self[1])+" "+str(self[2])+" "+str(self[3])
    
    def dot(self, other):
        return self[0]*other[0] + self[1]*other[1] + self[2]*other[2]