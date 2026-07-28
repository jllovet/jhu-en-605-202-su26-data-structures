import unittest
import lab3.huffman.encoding.tree as tree


class TestIteration(unittest.TestCase):
    def test_preorder_single_node(self):
        root = tree.Node(parent=None, data="A")
        self.assertEqual(["A"], list(root.preorder()))

    def test_inorder_single_node(self):
        root = tree.Node(parent=None, data="A")
        self.assertEqual(["A"], list(root.inorder()))

    def test_postorder_single_node(self):
        root = tree.Node(parent=None, data="A")
        self.assertEqual(["A"], list(root.postorder()))

    def test_preorder_two_nodes(self):
        root = tree.Node(parent=None, data="A")
        b = tree.Node(parent=root, data="B")
        root.left = b
        self.assertEqual(["A", "B"], list(root.preorder()))

    def test_inorder_two_nodes(self):
        root = tree.Node(parent=None, data="A")
        b = tree.Node(parent=root, data="B")
        root.left = b
        self.assertEqual(["B", "A"], list(root.inorder()))

    def test_postorder_two_nodes(self):
        root = tree.Node(parent=None, data="A")
        b = tree.Node(parent=root, data="B")
        root.left = b
        self.assertEqual(["B", "A"], list(root.postorder()))

    def test_preorder_three_nodes(self):
        root = tree.Node(parent=None, data="A")
        b = tree.Node(parent=root, data="B")
        root.left = b
        c = tree.Node(parent=root, data="C")
        root.right = c
        self.assertEqual(["A", "B", "C"], list(root.preorder()))

    def test_inorder_three_nodes(self):
        root = tree.Node(parent=None, data="A")
        b = tree.Node(parent=root, data="B")
        root.left = b
        c = tree.Node(parent=root, data="C")
        root.right = c
        self.assertEqual(["B", "A", "C"], list(root.inorder()))

    def test_postorder_three_nodes(self):
        root = tree.Node(parent=None, data="A")
        b = tree.Node(parent=root, data="B")
        root.left = b
        c = tree.Node(parent=root, data="C")
        root.right = c
        self.assertEqual(["B", "C", "A"], list(root.postorder()))


class TestIterationWithThreeLevels(unittest.TestCase):
    def setUp(self):
        root = tree.Node(parent=None, data="A")
        b = tree.Node(parent=root, data="B")
        root.left = b
        c = tree.Node(parent=root, data="C")
        root.right = c
        # children of b
        d = tree.Node(parent=b, data="D")
        b.left = d
        e = tree.Node(parent=b, data="E")
        b.right = e
        # children of c
        f = tree.Node(parent=c, data="F")
        c.left = f
        g = tree.Node(parent=c, data="G")
        c.right = g
        self.tree = root

    def test_preorder_three_levels(self):
        self.assertEqual("ABDECFG", self.tree.preorder_as_str())

    def test_inorder_three_levels(self):
        self.assertEqual("DBEAFCG", self.tree.inorder_as_str())

    def test_postorder_three_levels(self):
        self.assertEqual("DEBFGCA", self.tree.postorder_as_str())
