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

    def test_push_returns_true_if_successful(self):
        self.assertTrue(self.stack.push("a"))
    
    def test_push_returns_false_if_stack_has_0_capacity(self):
        zero_stack = s.Stack(0)
        self.assertFalse(zero_stack.push("a"))
    
    def test_push_returns_false_if_stack_is_full(self):
        for i in range(0,10):
            self.bounded_stack.push("a")
        self.assertEqual(self.bounded_stack.height, 10)
        self.assertEqual(self.bounded_stack.max_height, 10)
        self.assertFalse(self.bounded_stack.push("a"))



if __name__ == "__main__":
    unittest.main()