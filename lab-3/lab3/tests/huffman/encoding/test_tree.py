import unittest
import lab3.huffman.encoding.tree as tree
from lab3.huffman.encoding.encode import EncodingData
from lab3.huffman.encoding.tree import MinHeap


class TestMinHeap(unittest.TestCase):
    def test_enqueue(self):
        h = MinHeap()
        a = EncodingData(characters="A", score=1)
        b = EncodingData(characters="B", score=2)
        c = EncodingData(characters="C", score=0)
        d = EncodingData(characters="D", score=3)
        e = EncodingData(characters="E", score=2)
        h.enqueue(a)
        self.assertListEqual([a], h.data)

        h.enqueue(b)
        self.assertListEqual([a, b], h.data)

        h.enqueue(c)
        self.assertListEqual([c, b, a], h.data)

        h.enqueue(d)
        self.assertListEqual([c, b, a, d], h.data)

        h.enqueue(e)
        self.assertListEqual([c, b, a, d, e], h.data)

    def test_dequeue(self):
        h = MinHeap()
        a = EncodingData(characters="A", score=2)
        b = EncodingData(characters="B", score=3)
        c = EncodingData(characters="C", score=0)
        d = EncodingData(characters="D", score=2)
        e = EncodingData(characters="E", score=3)
        h.enqueue(a)
        h.enqueue(b)
        h.enqueue(c)
        h.enqueue(d)
        h.enqueue(e)
        self.assertListEqual([c, d, a, b, e], h.data)

        current = h.dequeue()
        self.assertEqual(current, c)
        self.assertListEqual([a, d, e, b], h.data) #FIX HERE

        current = h.dequeue()
        self.assertEqual(current, a)
        self.assertListEqual([d, b, e], h.data)

        current = h.dequeue()
        self.assertEqual(current, d)
        self.assertListEqual([b, e], h.data)

        current = h.dequeue()
        self.assertEqual(current, b)
        self.assertListEqual([e], h.data)


class TestComparison(unittest.TestCase):
    def test_le_for_same_char_diff_score(self):
        a = EncodingData(characters="X", score=0)
        b = EncodingData(characters="X", score=1)
        self.assertTrue(a <= b)
        self.assertFalse(a == b)
        self.assertFalse(a > b)

    def test_le_for_same_char_same_score(self):
        a = EncodingData(characters="X", score=1)
        b = EncodingData(characters="X", score=1)
        self.assertTrue(a <= b)
        self.assertTrue(a == b)
        self.assertFalse(a > b)

    def test_lt_for_same_char_diff_score(self):
        a = EncodingData(characters="X", score=0)
        b = EncodingData(characters="X", score=1)
        self.assertTrue(a < b)
        self.assertFalse(a == b)
        self.assertFalse(a > b)

    def test_lt_for_same_char_same_score(self):
        a = EncodingData(characters="X", score=1)
        b = EncodingData(characters="X", score=1)
        self.assertFalse(a < b)
        self.assertTrue(a == b)
        self.assertFalse(a > b)

    def test_lt_for_diff_char_diff_score(self):
        a = EncodingData(characters="X", score=0)
        b = EncodingData(characters="Y", score=1)
        self.assertTrue(a < b)
        self.assertFalse(a == b)
        self.assertFalse(a > b)

    def test_lt_for_diff_char_same_score(self):
        a = EncodingData(characters="X", score=1)
        b = EncodingData(characters="Y", score=1)
        self.assertTrue(a < b)
        self.assertFalse(a == b)
        self.assertFalse(a > b)

    def test_lt_for_short_char_to_long_char_same_score(self):
        a = EncodingData(characters="X", score=1)
        b = EncodingData(characters="XY", score=1)
        self.assertTrue(a < b)
        self.assertFalse(a == b)
        self.assertFalse(a > b)

    def test_lt_for_short_char_to_long_char_diff_score(self):
        a = EncodingData(characters="X", score=2)
        b = EncodingData(characters="XY", score=1)
        self.assertFalse(a < b)
        self.assertFalse(a == b)
        self.assertTrue(a > b)

        a = EncodingData(characters="X", score=1)
        b = EncodingData(characters="XY", score=2)
        self.assertTrue(a < b)
        self.assertFalse(a == b)
        self.assertFalse(a > b)

    def test_lt_with_alphabetic_tie_breaker(self):
        a = EncodingData(characters="ABC", score=2)
        b = EncodingData(characters="XYZ", score=2)
        self.assertTrue(a < b)
        self.assertFalse(a == b)
        self.assertFalse(a > b)


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
