"""Singly-Linked List Demo Code
Code from: https://www.geeksforgeeks.org/python-linked-list/
"""


from typing import Any


class ListNode:
    """Node in a linked list
    """
    def __init__(self, val=0, next_node=None) -> None:
        self.val = val
        self.next: ListNode | None = next_node

    def __repr__(self) -> str:
        return str(self.val)

    def __eq__(self, node) -> bool:
        return self.val == node.val


class LinkedList:
    """Linked List data structure
    """
    def __init__(self) -> None:
        self.head = None

    def insert_at_start(self, data: Any) -> None:
        """Adds a new node to the start of the linked list

        Args:
            data (Any): The data to be added to the start
        """
        node: ListNode = ListNode(data)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def insert_at_index(self, data: Any, index: int) -> None:
        """Adds a new node to a specified index. Indexing starts from 0

        Args:
            data (Any): The data to be added to the linked list
            index (int): The index of the new node

        Raises:
            IndexError: If the index is out of range
        """
        node: ListNode = ListNode(data)
        if index == 0:
            self.insert_at_start(node)

        position: int = 0
        current_node: ListNode | None = self.head
        while (current_node is not None and position+1 != index):
            position += 1
            current_node = current_node.next

        if current_node is not None:
            node.next = current_node.next
            current_node.next = node
        else:
            raise IndexError("Index not present")

    def insert_at_end(self, data: Any) -> None:
        """Inserts a node to the end of the linked list

        Args:
            data (Any): The data to be added to the end of the linked list
        """
        node: ListNode = ListNode(data)
        if self.head is None:
            self.head = node
            return

        current_node: ListNode = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = node

    def update_node(self, val: Any, index: int) -> None:
        """Updates the value for a node at a specified index

        Args:
            val (Any): The new value
            index (int): The index of the node to be updated

        Raises:
            IndexError: If the index is out of range
        """
        current_node: ListNode = self.head
        position: int = 0
        if position == index:
            current_node.val = val
        else:
            while (current_node is not None and position != index):
                position += 1
                current_node = current_node.next

            if current_node.next is not None:
                current_node.val = val
            else:
                raise IndexError("Index not present")

    def remove_first_node(self) -> None:
        """Removes the first node from the linked list
        """
        if self.head is None:
            return

        self.head = self.head.next

    def remove_last_node(self) -> None:
        """Removes the last node from the linked list
        """
        if self.head is None:
            return

        current_node = self.head
        while(current_node is not None and current_node.next.next is not None):
            current_node = current_node.next

        current_node.next = None

    def remove_at_index(self, index: int) -> None:
        """Removes a node from a specified index

        Args:
            index (int): The index of the node to be removed

        Raises:
            IndexError: If the index is out of range
        """
        if self.head is None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node is not None and position+1 != index):
                position = position+1
                current_node = current_node.next

            if current_node is not None:
                current_node.next = current_node.next.next
            else:
                raise IndexError("Index not present")

    def remove_node(self, data: Any) -> None:
        """Removes a node of a specified value

        Args:
            data (Any): The value of the node to be removed
        """
        current_node = self.head

        if current_node.data == data:
            self.remove_first_node()
            return

        while(current_node is not None and current_node.next.data != data):
            current_node = current_node.next

        if current_node is None:
            return
        current_node.next = current_node.next.next

    def __len__(self) -> int:
        size = 0
        if self.head:
            current_node = self.head
            while current_node:
                size += 1
                current_node = current_node.next
            return size
        return 0

    def __repr__(self) -> str:
        current_node = self.head
        ll_str = ""
        while current_node:
            ll_str += str(current_node.val) + " "
            current_node = current_node.next
        return ll_str


if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_end('a')
    llist.insert_at_end('b')
    llist.insert_at_start('c')
    llist.insert_at_end('d')
    llist.insert_at_index('g', 2)
    print(len(llist))
    print(llist)
