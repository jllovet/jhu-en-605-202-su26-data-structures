import unittest
import lab1.stack as s

class TestStack(unittest.TestCase):
    def test_new_stack_is_empty(self):
        stack = s.Stack() # unbounded
        bounded_stack = s.Stack(10) # bounded
        self.assertTrue(stack.is_empty())
        self.assertTrue(bounded_stack.is_empty())
    
    def test_new_stack_is_not_full(self):
        stack = s.Stack() # unbounded
        bounded_stack = s.Stack(10) # bounded
        self.assertFalse(stack.is_full())
        self.assertFalse(bounded_stack.is_full())
    
    def test_empty_stack_no_longer_empty_after_push(self):
        stack = s.Stack() # unbounded
        stack.push("a")
        self.assertFalse(stack.is_empty())

    def test_push_returns_true_if_successful(self):
        stack = s.Stack() # unbounded
        self.assertTrue(stack.push("a"))
    
    def test_push_increments_stack_height(self):
        stack = s.Stack() # unbounded
        self.assertEqual(stack.height,0)
        stack.push("a")
        self.assertEqual(stack.height,1)
    
    def test_push_returns_false_if_stack_has_0_capacity(self):
        zero_stack = s.Stack(0)
        self.assertFalse(zero_stack.push("a"))
    
    def test_push_returns_false_if_stack_is_full(self):
        bounded_stack = s.Stack(10) # bounded
        for i in range(0,10):
            bounded_stack.push("a")
        self.assertEqual(bounded_stack.height, 10)
        self.assertEqual(bounded_stack.max_height, 10)
        self.assertFalse(bounded_stack.push("a"))

    def test_pop_returns_element_from_top_of_non_empty_stack(self):
        stack = s.Stack()
        stack.push("a")
        self.assertEqual(stack.pop(), "a")


if __name__ == "__main__":
    unittest.main()