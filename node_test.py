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

if __name__ == '__main__':
    unittest.main()
