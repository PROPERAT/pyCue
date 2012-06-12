from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from Material import *
from numpy import matrix

class OpenGLDriver:
    def __init__(self):
        self.driver_name = "OGL_Fixed_Pipeline"
        self.current_material = None
        
        self.projection_matrix = None
        self.lookat_matrix  = None
    
    def start_video(self):
        self.windowSizeX = 800
        self.windowSizeY = 600
        self.windowSurface = pygame.display.set_mode((self.windowSizeX, self.windowSizeY), pygame.HWSURFACE | pygame.OPENGL | pygame.DOUBLEBUF)
        pygame.display.set_caption("pyCue")
        self.prepare_opengl()
    
    def prepare_opengl(self):
        glClearColor(0,0,0,0)
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
    
    def render_camera(self, camera, debug_flag):
        self.projection_matrix = camera.get_projection()
        self.lookat_matrix = camera.get_lookat()
        
        glMatrixMode(GL_PROJECTION)
        glLoadMatrixf(self.projection_matrix.flatten('F').tolist()[0])
        
    def set_material(self, material):
        if self.current_material == material:
            return
        else:
            self.current_material.unset_material(self)
            self.current_material = material
            self.current_material.set_material(self)
    
    def render_node(self, node):
        #Prepare matrices
        #temp = node.get_absolute_transformation()
        glMatrixMode(GL_MODELVIEW)
        glLoadMatrixf(self.lookat_matrix.flatten('F').tolist()[0])
        #glMultMatrixf(node.get_absolute_transformation().flatten('F').tolist()[0])
        
        #setup material
        #self.set_material(node.get_material())
        
        #render the mesh
        self.render_mesh(node.get_mesh())
    
    def render_mesh(self, mesh):
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointerf(mesh.get_vertices())
        glDrawElementsui(GL_TRIANGLES, mesh.get_indices())
        glDisableClientState(GL_VERTEX_ARRAY)