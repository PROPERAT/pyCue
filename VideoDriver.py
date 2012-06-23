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
        glEnable(GL_TEXTURE_2D)
        
    def render_camera(self, camera, debug_flag):
        self.projection_matrix = camera.get_projection()
        self.lookat_matrix = camera.get_lookat()
        glMatrixMode(GL_PROJECTION)
        glLoadMatrixf(self.projection_matrix.flatten('F').tolist()[0])
          

    def render_node(self, node):
        #Prepare matrices
        #temp = node.get_absolute_transformation()
        glMatrixMode(GL_MODELVIEW)
        glLoadMatrixf(self.lookat_matrix.flatten('F').tolist()[0])
        glMultMatrixf(node.get_absolute_transformation().flatten('F').tolist()[0])
        
        #setup material
        #self.set_material(node.get_material())
        
        #render the mesh
        self.render_mesh(node.get_mesh())
    
    def render_mesh(self, mesh):
        glColor3f(1,1,1)
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointerf(mesh.get_vertices())
        
        if mesh.has_text_coords():
            glEnableClientState(GL_TEXTURE_COORD_ARRAY)
            glTexCoordPointerf(mesh.get_text_coords())
        glDrawElementsui(GL_TRIANGLES, mesh.get_indices())
        
        if mesh.has_text_coords():
            glDisableClientState(GL_TEXTURE_COORD_ARRAY)
        glDisableClientState(GL_VERTEX_ARRAY)