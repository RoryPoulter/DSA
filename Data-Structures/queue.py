"""Demo code for the queue data structure
"""


class Queue:
    """Queue data structure. Can store `n - 1` values. Allows wrap-around.
    """
    def __init__(self, size: int) -> None:
        if size < 2:
            raise ValueError("'size' must be greater than 1")
        self.data = [None] * size   # The data in the queue
        self.f = 0                  # Index of the front of the queue
        self.r = 0                  # Index of the rear of the queue
        self.n = size               # The size of the queue

    def __repr__(self):
        return str(self.data)

    def isEmpty(self) -> bool:
        """Method for determining if the queue is empty. If the points `f` an `r` are the same then
        the queue is empty.
        
        O(1)

        Returns:
            bool: If the queue is empty
        """
        return self.f == self.r

    def isFull(self) -> bool:
        """Method for determining if the queue is full. Can only store `n - 1` values to prevent
        full and empty state being identical.

        O(1)

        Returns:
            bool: If the queue is full
        """
        return (self.r + 1) % self.n == self.f

    def enqueue(self, val) -> None:
        """Method for enqueuing values into the rear of the queue.

        O(1)

        Args:
            val (any): The value to be enqueued

        Raises:
            ValueError: If the queue is full
        """
        if self.isFull():
            raise ValueError("Cannot enqueue value: queue is full")
        self.data[self.r] = val
        self.r  = (self.r + 1) % self.n

    def dequeue(self):
        """Method for dequeuing items from the front of the queue.

        O(1)

        Raises:
            ValueError: If the queue is empty

        Returns:
            Any: The value at the front of the queue
        """
        if self.isEmpty():
            raise ValueError("Cannot dequeue: queue is empty")
        val = self.data[self.f]
        self.data[self.f] = None
        self.f  = (self.f + 1) % self.n
        return val

    def front(self):
        """Method for returning the value at the front of the queue without dequeuing it.

        Returns:
            Any: The value at the front of the queue.
        """
        return self.data[self.f]


if __name__ == "__main__":
    # Initialise the queue
    q = Queue(5)
    print(q.isEmpty())
    print(q)
    q.enqueue(10)
    q.enqueue(15)
    q.enqueue(5)
    q.dequeue()
    print(q)
    q.dequeue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    print(q.isFull())
