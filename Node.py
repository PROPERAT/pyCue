from numpy import *
from Vector import *
from Utility_functions import *

class Node():
    def __init__(self, node_ID):
        if node_ID <= 0:
            raise ArithmeticError('\nThe number must be greater than zero! \n')
        self.ID = node_ID
        self.name = ''
        self.bounding_box = None
        self.transformed_bounding_box = None
        self.absolute_transformation = get_identity_matrix()
        self.relative_transformation = get_identity_matrix()
        self.visible = False
        self.children = []
        self.scale = get_zero_vector()
        self.rotation = get_zero_vector()
        self.translation = get_zero_vector()
        self.absolute_position = get_identity_matrix()
        self.parent = None
        self.debug_info_visible = False
        self.mesh = None
        

    #function called when node is registered in SceneNodeManager
    def on_register_node(self):
        pass
    
    #function called when node is rendered
    def render(self):
        pass
    
    #returns name of the node
    def get_name(self):
        return self.name
    
    #sets name of the node
    def set_name(self, string):
        self.name = string
    
    #returns the AABB of the node
    def get_bounding_box(self):
        pass
    
    #returns the transormed AABB. Transformation is done with the absolute transformation
    def get_transformed_bounding_box(self):
        pass
    
    #returns the absolute transformation in matrix form
    def get_absolute_transformation(self):
        if self.parent != None:
            return parent.get_absolute_transformation()*self.get_relative_transformation()
        else:
            return self.get_relative_transformation()
    
    #returns relative transformation in matrix form
    def get_relative_transformation(self):
        return self.relative_transformation
    
    #returns true if node is visible
    def is_visible(self):
        return self.visible
    
    #sets visibility
    def set_visible(self, bool):
        self.visible = bool
    
    #returns ID - numerical value
    def get_ID(self):
        return self.ID
    
    #sets ID - numerical value
    def set_ID(self):
        pass
    
    #adds a child node to the current node
    def add_child(self, node):
        self.children.append(node)
        node.parent = self

    def get_children(self):
        return self.children
    
    #removes a child node
    def remove_child(self, node):
        node.parent = None
        self.children.remove(node)
    
    #removes all children
    def remove_all_children(self):
        for child in self.children:
            child.parent = None
        self.children = []
    
    #removes this node if attached to any other
    def remove(self):
        pass
    
    #returns scale factor of node as vector
    def get_scale(self):
        return self.scale
    
    #sets scale factor of node as vector
    def set_scale(self, vector):
        self.scale = vector
        self.relative_transformation = self.relative_transformation * scale_matrix(vector)
    
    #returns rotation of node as vector of x,y,z degrees rotations
    def get_rotation(self):
        return self.rotation
    
    #sets rotation of node as vector of x,y,z degrees rotations
    def set_rotation(self, vector):
        self.rotation = vector
        self.relative_transformation = self.relative_transformation * rotation_matrix(vector)
    
    #sets translation of node as vector of x,y,z
    def set_translation(self, vector):
        self.translation = vector
    
    #sets translation of node as vector of x,y,z
    def get_translation(self):
        return self.translation
    
    #returns position as vector
    def get_absolute_position(self):
        return self.absolutePosition
    
    #sets parent node
    def set_parent(self, node):
        self.parent = node
        node.add_child(self)
    
    #recalculates absolute position
    def update_absolute_position(self):
        pass
    
    #returns the parent node
    def get_parent(self):
        return self.parent
    
    #sets debug flag
    def set_debug_info_visible(self, bool):
        self.debug_info_visible = bool
    
    #gest debug flag
    def is_debug_info_visible(self):
        return self.debug_info_visible
    
    def set_mesh(self, mesh):
        self.mesh = mesh
        
    def get_mesh(self):
        return self.mesh
    