import pygame, sys
from OpenGL.GL import *
from OpenGL.GLU import *
from VideoDriver import *
from Node import *
from TestCubeMesh import *
from Camera import *
class GameEvent:
    def __init__(self, code):
        self.code = code
        

class PygameWindow:
    def __init__(self):
        pygame.init()
        self.key_states = [0 for i in range(0,512)]
        self.game_event_queue = []
        self.frame_time = 0
        self.last_time = 0
        self.eye_pos = (0,0,0)
        
        
    def push_game_event(self, event):
        self.game_event_queue.append(event)
        
    def start_main_loop(self):
        self.last_time  = pygame.time.get_ticks()
        while True:
            current_time = pygame.time.get_ticks()
            self.frame_time = current_time - self.last_time
            self.last_time = current_time
            
            self.process_system_events()
            self.read_user_input()
            self.process_game_events()
            self.update_game()
            self.render_window()
            pygame.display.flip()
    
    def process_system_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key >= 0 and event.key <= 512:
                    self.key_states[event.key] = True
            elif event.type == pygame.KEYUP:
                if event.key >= 0 and event.key <= 512:
                    self.key_states[event.key] = False
                    
    def read_user_input(self):
        for key, pressed in enumerate(self.key_states):
            if pressed:
                if key == ord('w'):
                    self.game_event_queue.append(GameEvent(1))
                elif key == ord('s'):
                    self.game_event_queue.append(GameEvent(2))

    def process_game_events(self):
        for event in self.game_event_queue:
            if event.code == 1:
                self.eye_pos = (self.eye_pos[0], self.eye_pos[1], self.eye_pos[2] -1)
            elif event.code == 2:
                self.eye_pos = (self.eye_pos[0], self.eye_pos[1], self.eye_pos[2] +1)
        del self.game_event_queue[:]
    
    def update_game(self):
        pass
        
    def render_window(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor4f(1,1,1,1)
        glLoadMatrixf([2,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])
        gluLookAt(self.eye_pos[0],self.eye_pos[1],self.eye_pos[2], self.eye_pos[0],self.eye_pos[1],self.eye_pos[2]-1, 0,1,0)
        
        pointer = [[0.0, 20.0, -50.0],[20.0, 20.0, -50.0],[20.0, 0.0, -50.0],[0.0, 0.0, -50.0]]
        
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointerf(pointer)
        glDrawElementsui(GL_QUADS, [0,1,2,3])      
        
#a = PygameWindow()
#a.start_main_loop()

n = Node(10)
n.set_mesh(TestCubeMesh())
d = OpenGLDriver()
d.start_video()
eye_pos = vector([25.0,10.0,-10.0,1.0])
c = Camera()
c.set_eye(eye_pos)
c.set_reference(vector([0,0,0,1]))
def process_system_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
while(1):
    process_system_events()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glEnable(GL_CULL_FACE)
    glColor4f(1,1,1,1)
    d.render_camera(c, 0)
    d.render_node(n)
    pygame.display.flip()