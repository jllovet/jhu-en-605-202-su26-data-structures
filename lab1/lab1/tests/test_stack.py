import unittest
import lab1.stack as s


class TestStack(unittest.TestCase):
    def test_new_stack_is_empty(self):
        stack = s.Stack()  # unbounded
        bounded_stack = s.Stack(10)  # bounded
        self.assertTrue(stack.is_empty())
        self.assertTrue(bounded_stack.is_empty())

    def test_new_stack_is_not_full(self):
        stack = s.Stack()  # unbounded
        bounded_stack = s.Stack(10)  # bounded
        self.assertFalse(stack.is_full())
        self.assertFalse(bounded_stack.is_full())

    def test_empty_stack_no_longer_empty_after_push(self):
        stack = s.Stack()  # unbounded
        stack.push("a")
        self.assertFalse(stack.is_empty())
    
    def test_stack_height_and_size_of_data_are_in_sync(self):
        stack = s.Stack()  # unbounded
        self.assertEqual(stack.height, 0)
        self.assertEqual(len(stack.data), 0)
        self.assertEqual(stack.height, len(stack.data))
        stack.push("a")
        self.assertEqual(stack.height, 1)
        self.assertEqual(len(stack.data), 1)
        self.assertEqual(stack.height, len(stack.data))
        stack.pop()
        self.assertEqual(stack.height, 0)
        self.assertEqual(len(stack.data), 0)
        self.assertEqual(stack.height, len(stack.data))

    def test_stack_becomes_full_when_max_height_is_reached(self):
        stack = s.Stack(1)  # bounded
        self.assertFalse(stack.is_full())
        self.assertTrue(stack.is_empty())
        stack.push("a")
        self.assertTrue(stack.is_full())
        self.assertFalse(stack.is_empty())

    def test_push_returns_None_if_successful(self):
        stack = s.Stack()  # unbounded
        self.assertIsNone(stack.push("a"))

    def test_push_increments_stack_height(self):
        stack = s.Stack()  # unbounded
        self.assertEqual(stack.height, 0)
        stack.push("a")
        self.assertEqual(stack.height, 1)

    def test_push_raises_overflow_error_if_stack_has_0_capacity(self):
        zero_stack = s.Stack(0)
        with self.assertRaises(OverflowError):
            zero_stack.push("a")

    def test_push_raises_overflow_error_if_stack_is_full(self):
        bounded_stack = s.Stack(10)  # bounded
        for i in range(0, 10):
            bounded_stack.push("a")
        self.assertEqual(bounded_stack.height, 10)
        self.assertEqual(bounded_stack.max_height, 10)
        with self.assertRaises(OverflowError):
            bounded_stack.push("a")

    def test_push_on_full_stack_raises_overflow_error(self):
        bounded_stack = s.Stack(2)  # bounded
        bounded_stack.push("a")
        bounded_stack.push("b")
        with self.assertRaises(OverflowError):
            bounded_stack.push("c")

    def test_push_on_full_stack_does_not_change_height(self):
        bounded_stack = s.Stack(2)  # bounded
        bounded_stack.push("a")
        bounded_stack.push("b")
        self.assertEqual(bounded_stack.max_height, 2)
        self.assertEqual(bounded_stack.height, 2)
        self.assertEqual(bounded_stack.max_height, bounded_stack.height)
        try:
            bounded_stack.push("c")
        except OverflowError:
            pass
        self.assertEqual(bounded_stack.max_height, 2)
        self.assertEqual(bounded_stack.height, 2)
        self.assertEqual(bounded_stack.max_height, bounded_stack.height)

    def test_pop_returns_element_from_top_of_non_empty_stack(self):
        stack = s.Stack()
        stack.push("a")
        self.assertEqual(stack.pop(), "a")

    def test_pop_returns_None_from_top_of_empty_stack(self):
        stack = s.Stack()
        self.assertIsNone(stack.pop())

    def test_pop_decrements_stack_height(self):
        stack = s.Stack()
        stack.push("a")
        self.assertEqual(stack.height, 1)
        stack.pop()
        self.assertEqual(stack.height, 0)

    def test_pop_on_empty_does_not_affect_height(self):
        stack = s.Stack()
        self.assertEqual(stack.height, 0)
        stack.pop()
        self.assertEqual(stack.height, 0)


if __name__ == "__main__":
    unittest.main()
