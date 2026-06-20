import unittest
import lab1.stack as s

class TestStack(unittest.TestCase):
    def setUp(self):
        print("setting up stack for tests")
        self.stack = s.Stack() # unbounded
        self.bounded_stack = s.Stack(10) # bounded

    def test_new_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.assertTrue(self.bounded_stack.is_empty())
    
    def test_new_stack_is_not_full(self):
        self.assertFalse(self.stack.is_full())
        self.assertFalse(self.bounded_stack.is_full())


if __name__ == "__main__":
    unittest.main()