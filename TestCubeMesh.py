from numpy import *
from math import *


class TestCubeMesh:
    def __init__(self):
        self.vertices = []
        self.indices = []
        self.normals = []
        self.text_coord = []
        self.create_mesh()
        
    def gen_uv(self, point):
        t_u = 0.0
        t_v = 0.0
        if fabs(point[0]) > fabs(point[1]) and fabs(point[0]) > fabs(point[2]):
            t_u = copysign(point[2], point[0])
            t_v = - point[1]
        elif fabs(point[1]) > fabs(point[0]) and fabs(point[1]) > fabs(point[2]):
            t_u = point[2]
            t_v = copysign(point[0], point[1])
        elif fabs(point[2]) > fabs(point[0]) and fabs(point[2]) > fabs(point[1]):
            t_u = - copysign(point[0], point[2])
            t_v = - point[1]
        u = (t_u + 1) * 0.5
        v = (t_v + 1) * 0.5
        return [u, v, 0]
        
    def create_mesh(self):
        radius = 1
        
        self.vertices.append([radius, 0, 0])
        self.text_coord.append(self.gen_uv(self.vertices[len(self.vertices) - 1]))
        self.vertices.append([- radius, 0, 0])
        self.text_coord.append(self.gen_uv(self.vertices[len(self.vertices) - 1]))
        
        pieces = 20
        for x in range(0, pieces):
            inner_distance = radius - (x+1)*2*radius/(pieces+1)
            inner_radius = sqrt(radius**2 - inner_distance**2)
            for y in range(0, pieces):
                self.vertices.append([inner_distance, inner_radius * math.sin((y/pieces)*2*pi), inner_radius * math.cos((y/pieces)*2*pi)])
                self.text_coord.append(self.gen_uv(self.vertices[len(self.vertices) - 1]))
        
        count_of_points = pieces*pieces + 2
        
        for i in range(2, pieces+1):
            self.indices.append([0, i, i + 1])
        
        self.indices.append([0, 2, pieces + 1])
        
        for i in range(count_of_points - pieces, count_of_points-1 ):
            self.indices.append([1, i, i + 1])
        
        self.indices.append([1, count_of_points-1, count_of_points - pieces])
        
        for i in range(0, pieces-1):
            for y in range(0, pieces):
                if y != pieces-1:
                    self.indices.append([2+pieces*i +y, 2+pieces*(i+1) +y, 2+pieces*i+y+1])
                    self.indices.append([2+pieces*i+y+1, 2+pieces*(i+1) +y, 2+pieces*(i+1) +y+1])
                else:
                    self.indices.append([2+pieces*i +y, 2+pieces*(i+1) +y, 2+pieces*i])
                    self.indices.append([2+pieces*i, 2+pieces*(i+1) +y, 2+pieces*(i+1)])
                    
    def get_indices(self):
        return self.indices
        
    def get_vertices(self):
        return self.vertices
    
    def get_text_coords(self):
        return self.text_coord
        
    def has_text_coords(self):
        return True
        