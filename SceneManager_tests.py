import unittest
from SceneManager import *

class SceneManagerTests(unittest.TestCase):
    def test_constructor(self):
        scene_manager = SceneManager()
        assert(scene_manager is not None)
        
    def test_get_root(self):
        scene_manager = SceneManager()
        root_tester = scene_manager.get_root_node()
        assert(root_tester == scene_manager.get_root_node() and root_tester is scene_manager.get_root_node())
    
    def test_create_nodes(self):
        number_of_nodes_to_test = 5
        test_nodes = []
        scene_manager = SceneManager()
        for i in range(0,number_of_nodes_to_test):
            test_nodes.append(scene_manager.create_node())
        
        test_result = True
        for i in range(0,number_of_nodes_to_test-1):
            for j in range(i+1, number_of_nodes_to_test):
                if test_nodes[i].get_ID() == test_nodes[j].get_ID():
                    assert(False and "Created nodes with same IDs!")
    
    def test_add_nodes(self):   
        scene_manager = SceneManager()
        
        first_child = scene_manager.create_node()
        second_child = scene_manager.create_node()
        
        scene_manager.add_scene_node(node=first_child)
        scene_manager.add_scene_node(node=second_child, parent=first_child)
        
    def test_search_by_ID(self):
        scene_manager = SceneManager()
        
        first_child = scene_manager.create_node()
        scene_manager.add_scene_node(node=first_child)
        
        node1 = scene_manager.get_node_from_ID(first_child.get_ID())
        
        assert(node1 == first_child and node1 is first_child)
        
    def test_search_by_name(self):
        test_name = "Find_me!"
        scene_manager = SceneManager()
        
        first_child = scene_manager.create_node()
        second_child = scene_manager.create_node()
        second_child.set_name(test_name)
        
        scene_manager.add_scene_node(node=first_child)
        scene_manager.add_scene_node(node=second_child, parent=first_child)
        node1 = scene_manager.get_node_from_name(test_name)
        
        assert(node1 == second_child and node1 is second_child)
        
if __name__ == '__main__':
    unittest.main()
