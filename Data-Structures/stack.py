"""Demo code for stacks
"""


class Stack:
    """Stack data structure
    """
    def __init__(self):
        self.size = -1
        self.data = []

    def __repr__(self):
        return str(self.data)

    def isEmpty(self) -> bool:
        """Checks if the stack is empty

        Returns:
            bool: If the stack is empty
        """
        return self.size == -1

    def push(self, val) -> None:
        """Pushes a value to the top of the stack

        Args:
            val (any): The value to be pushed to the top of the stack
        """
        self.data.append(val)
        self.size += 1

    def pop(self):
        """Removes the value from the top of the stack

        Raises:
            ValueError: If the stack is empty

        Returns:
            any: The value at the top of the stack
        """
        if self.isEmpty():
            raise ValueError("Unable to pop from stack: stack is empty")
        self.size -= 1
        return self.data.pop()

    def top(self):
        """Returns the top value from the stack without removing it

        Raises:
            ValueError: If the stack is empty

        Returns:
            any: The top value of the stack
        """
        if self.isEmpty():
            raise ValueError("Unable to return top item from stack: stack is empty")
        return self.data[self.size]


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(13)
    print(s)
    s.pop()
    s.push(6)
    s.push(4)
    print(s)
