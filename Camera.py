from Vector import *
from numpy import float32, matrix
class Camera:
    def __init__(self):
        self.fovy = float32(45.0)
        self.aspect = float32(1.3)
        self.z_near = float32(1.0)
        self.z_far = float32(100.0)
        
        self.eye = vector([0.0,0.0,0.0,1.0])
        self.reference = vector([0.0,0.0,0.0,1.0])
        self.up = vector([0.0,1.0,0.0,1.0])
        
    def set_fovy(self, fov):
        self.fovy = float32(fov)
    def get_fovy(self):
        return self.fovy
    def set_aspect(self, aspect):
        self.aspect = float32(aspect)
    def get_aspect(self):
        return self.aspect
    def set_z_near(self, near):
        self.z_near = float32(near)
    def get_z_near(self):
        return self.z_near
    def set_z_far(self, far):
        self.z_far = float32(far)
    def get_z_far(self):
        return self.z_far
    def set_eye(self, eye):
        self.eye = eye
    def get_eye(self):
        return self.eye
    def set_reference(self, ref):
        self.reference = ref
    def get_reference(self):
        return self.reference
    def set_up(self, up):
        self.up = up
    def get_up(self):
        return self.up
    def get_projection(self):
        f = float32(1/math.tan(math.radians(self.fovy/2)))
        dist = self.z_near - self.z_far
        result = matrix([[float32(0) for i in range(0,4)] for j in range(0,4)])
        result.itemset((0,0), f/self.aspect)
        result.itemset((1,1), f)
        result.itemset((2,2), (self.z_far + self.z_near)/dist)
        result.itemset((2,3), (2 * self.z_far * self.z_near)/dist)
        result.itemset((3,2), -1)
        return result
    
    def get_lookat(self):
        F = self.reference - self.eye
        F.normalize()
        self.up.normalize()
        s = F.cross(self.up)
        u = s.cross(F)
        result = matrix([[s.x,s.y,s.z,0.0],[u.x,u.y,u.z,0.0],[-F.x,-F.y,-F.z,0.0],[0.0,0.0,0.0,1.0]])
        position_m = matrix([[1.0,0.0,0.0,-self.eye.x],[0.0,1.0,0.0,-self.eye.y],[0.0,0.0,1.0,-self.eye.z],[0.0,0.0,0.0,1.0]])
        return result*position_m

        