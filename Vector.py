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
    
    def __add__(self, other):
        return vector([self.x+other.x, self.y+other.y, self.z+other.z, 1.0])
    def __sub__(self, other):
        return vector([self.x-other.x, self.y-other.y, self.z-other.z, 1.0])
    def __mul__(self, other):
        return vector([self.x*other, self.y*other, self.z*other, 1.0])
    def __getattr__(self, name):
        if name == 'x':
            return self[0]        
        elif name == 'y':
            return self[1]
        elif name == 'z':
            return self[2]
        elif name == 'w':
            return self[3]
        else:
            raise AttributeError("No such attribute",name)
    
    def __setattr__(self, name, value):
        if name == 'x':
            self[0] = value
        elif name == 'y':
            self[1] = value
        elif name == 'z':
            self[2] = value
        elif name == 'w':
            self[3] = value
        else:
            self.__dict__[name] = value
        
    
    def __array_finalize__(self, obj):
        pass
        
    def __getitem__(self, pos):
        return self.item(pos)
        
    def __setitem__(self, pos, val):
        self.itemset(pos, val)
    
    def __repr__(self):
        return "vector("+str(self.x)+","+str(self.y)+","+str(self.z)+","+str(self.w)+")"
        
    def __str__(self):
        return "vector("+str(self.x)+","+str(self.y)+","+str(self.z)+","+str(self.w)+")"
    
    def dot(self, other):
        return self[0]*other[0] + self[1]*other[1] + self[2]*other[2]
        
    def cross(self, other):
        return vector([self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y - self.y*other.x, float32(1.0)])
    
    def normalize(self):
        len = float32(math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z))
        self.x /= len
        self.y /= len
        self.z /= len