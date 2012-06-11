class TestCubeMesh:
    def __init__(self):
        self.vertices = []
        self.indices = []
        self.normals = []
        self.create_mesh()
        
    def create_mesh(self):
        size = 1.0
        
        self.vertices.append([-size, -size, size])
        self.vertices.append([size, -size, size])
        self.vertices.append([size, size, size])
        self.vertices.append([-size, size, size])
        self.vertices.append([-size, -size, -size])
        self.vertices.append([size, -size, -size])
        self.vertices.append([size, size, -size])
        self.vertices.append([-size, size, -size])
        
        self.indices.append([0,1,2])
        self.indices.append([0,2,3])
        self.indices.append([4,5,6])
        self.indices.append([4,6,7])
        self.indices.append([3,2,6])
        self.indices.append([3,6,7])
        self.indices.append([0,1,5])
        self.indices.append([0,5,4])
        self.indices.append([1,5,6])
        self.indices.append([1,6,2])
        self.indices.append([0,4,7])
        self.indices.append([0,7,3])
        
    def get_indices(self):
        return self.indices
        
    def get_vertices(self):
        return self.vertices
        