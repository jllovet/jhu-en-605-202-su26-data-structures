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
    
    def test_empty_stack_no_longer_empty_after_push(self):
        self.stack.push("a")
        self.assertFalse(self.stack.is_empty())


if __name__ == "__main__":
    unittest.main()