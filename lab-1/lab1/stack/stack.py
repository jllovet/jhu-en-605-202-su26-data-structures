class Stack:
    """Implementation of the ADT Stack, using arrays for the underlying data"""
    def __init__(self, max_height: int = -1):
        """Initializes an empty stack with optional maximum height specified

        Args:
            max_height: int specifying maximum height of stack. If max_height
            is a nonnegative integer, then max_height is the maximum height
            for the stack. If max_height < 0, then the stack is unbounded.

        Returns:
            Stack initialized with empty data and maximum height set to max_height
        
        Raises:
            None

        Side Effects:
            None
        
        Idempotent:
            True
        """
        self.max_height = max_height
        self.data = []
        self.height = len(self.data)

    def is_empty(self) -> bool:
        """Returns a bool indicating whether the stack has no elements

        Args:
            None

        Returns:
            Bool indicating whether the stack has no elements
        
        Raises:
            None

        Side Effects:
            None
        
        Idempotent:
            True
        """
        return len(self.data) == 0

    def is_full(self) -> bool:
        """Returns a bool indicating whether the stack is at its max capacity

        If the stack is full, then an attempt to push an element onto it will
        result in an error.

        Args:
            None

        Returns:
            Bool indicating whether the stack's height is equal to its max_height
        
        Raises:
            None

        Side Effects:
            None
        
        Idempotent:
            True
        """
        return self.height == self.max_height
    
    def contains(self, item) -> bool:
        """Returns a bool indicating whether the item provided is in the stack

        Args:
            item: of any type

        Returns:
            Bool indicating whether the item provided is in the stack
        
        Raises:
            None

        Side Effects:
            None
        
        Idempotent:
            True
        """
        return item in self.data

    def peek(self) -> str | int | None:
        """Returns the value at the top of the stack without removing it

        Used to check what the value is at the top of the stack, often while
        performing a validation or check, without removing the item to be
        processed, in contrast to the pop method.

        Args:
            None

        Returns:
            str | int | None according to what was at the top of the stack
        
        Raises:
            None

        Side Effects:
            None
        
        Idempotent:
            True
        """
        if self.is_empty():
            return None
        idx = len(self.data) - 1 # end of the array
        return self.data[idx]
    
    def pop(self) -> str | int | None:
        """Removes the top value from the stack and returns it

        Used when processing elements from the stack. It will return the
        top element of the stack and will remove it to be processed, in
        contrast to the peek method. Pop will decrement the height of the
        stack if there were any items in it. If the stack is empty, there
        will be no effect.

        Args:
            None

        Returns:
            str | int according to what was at the top of the stack, or
            None if the stack was empty
        
        Raises:
            None

        Side Effects:
            Removes top element from the stack if the stack was not empty
            Decrements the height of the stack if the stack was not empty
        
        Idempotent:
            False
        """
        if self.data == []:
            return None
        self.height -= 1
        return self.data.pop()

    def push(self, item: str | int) -> None:
        """Adds item to the top of the stack if the stack is not full

        Push adds item to the top of the stack and increments the height of
        the stack, if the stack is not full. If the stack is full, then
        push will raise an OverFlowError. If item is not of type str or int,
        then push will raise a ValueError.

        Args:
            None

        Returns:
            str | int | None according to what was at the top of the stack
        
        Raises:
            OverflowError if the stack is already full
            ValueError if item is not of type str or int

        Side Effects:
            Adds an element to the top of the stack if it is not full
            Increments the height of the stack if it is not full
            Raises errors as described above
        
        Idempotent:
            False
        """
        if self.height == self.max_height:
            raise OverflowError("cannot push onto stack because it is full")
        if not isinstance(item, str | int):
            raise ValueError(f"cannot push onto stack because {item} is not of type str or int")
        self.data.append(item)
        self.height += 1
        return None
