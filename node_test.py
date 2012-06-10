import unittest
from Node import *

class NodeTest(unittest.TestCase):
    def test_node_ID(self):
        self.assertRaises(ArithmeticError, Node, 0)
        self.assertRaises(ArithmeticError, Node, -1)

    def test_set_get_node_methods(self):
        node = Node(5)
        self.assertEqual(5, node.get_ID())
        self.assertEqual('', node.get_name())
        node.set_name('new_name')
        self.assertEqual('new_name', node.get_name())
    
    def test_add_children(self):    
        node1 = Node(10)
        node2 = Node(11)
        to_test = Node(1)
        
        to_test.add_child(node1)
        to_test.add_child(node2)
        
        self.assertEqual(len(to_test.get_children()), 2)
        
        self.assertEqual(node1.get_parent(), to_test)
        self.assertEqual(node2.get_parent(), to_test)
    
    def test_remove_all_children(self):    
        node1 = Node(10)
        node2 = Node(11)
        to_test = Node(1)
        
        to_test.add_child(node1)
        to_test.add_child(node2)
        
        to_test.remove_all_children()
        
        self.assertEqual(len(to_test.get_children()), 0)
        
        self.assertIs(node1.get_parent(), None)
        self.assertIs(node2.get_parent(), None)
        
    def test_remove_child(self):    
        node1 = Node(10)
        node2 = Node(11)
        to_test = Node(1)
        
        to_test.add_child(node1)
        to_test.add_child(node2)
        
        to_test.remove_child(node1)
        
        self.assertNotIn(node1, to_test.get_children())
        
        self.assertIs(node1.get_parent(), None)
        
    def test_set_parent(self):
        parent = Node(1)
        child =  Node(2)
        
        child.set_parent(parent)
        
        self.assertEqual(child.get_parent(), parent)
        self.assertIn(child, parent.get_children())
        
    def test_visibility_flag(self):
        node = Node(1)
        node.set_visible(True)
        
        self.assertTrue(node.is_visible())
        
        node.set_visible(False)
        
        self.assertFalse(node.is_visible())


if __name__ == '__main__':
    unittest.main()
