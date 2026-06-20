import unittest
import lab1.stack as s

class TestStack(unittest.TestCase):
    def setUp(self):
        print("setting up stack for tests")
        self.stack = s.Stack(-1) # unbounded

    def test_new_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty())


if __name__ == "__main__":
    unittest.main()