from Node import *

class SceneManagerError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class SceneManager:
    def __init__(self):
        self.root_node = Node(1)
        self.root_node.set_name("scene_root")
        self.node_enumerator = 1
        self.active_camera = -1
        self.camera_lsit = []
        self.render_lsit = []
    
    def add_scene_node(self, node, parent=0):
        if parent == 0:
            self.root_node.add_child(node)
        else:
            if self.get_node_from_ID(parent.get_ID()) is None:
                raise SceneManagerError("Could not add node with parent who is not in the scene !")
            else:
                parent.add_child(node)
    
    def get_root_node(self):
        return self.root_node
    
    def get_node_from_ID(self, id, start=0):
        if start == 0:
            start = self.root_node
        
        if start.get_ID() == id:
            return start
        
        else:
            children_list = start.get_children()
            for child in children_list:
                return self.get_node_from_ID(id, child)
    
    def get_node_from_name(self, name, start=0):
        if start == 0:
            start = self.root_node
        
        if start.get_name() == name:
            return start
        
        else:
            children_list = start.get_children()
            for child in children_list:
                return self.get_node_from_name(name, child)
    
    def remove_all(self):
        self.root_node.remove_all()
        del self.camera_list[:]
        slef.active_camera = -1
    
    def register_video_driver(self, driver):
        self.video_driver = driver
        
    def get_active_camera(self):
        if self.active_camera != -1:
            return self.camera_list[active_camera]
    
    def register_node_for_rendering(self,node):
        render_list.append(node)
    
    def create_node(self):
        self.node_enumerator += 1
        return Node(self.node_enumerator)
