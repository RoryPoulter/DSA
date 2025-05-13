"""Demo code for tree data structure
"""


class Node:
    """Tree node class
    """
    def __init__(self, val):
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None

    # Comparative operations
    def __eq__(self, node) -> bool:
        if isinstance(node, Node):
            return self.val == node.val
        return self.val == node

    def __ne__(self, node) -> bool:
        if isinstance(node, Node):
            return self.val != node.val
        return self.val != node

    def __lt__(self, node) -> bool:
        if isinstance(node, Node):
            return self.val < node.val
        return self.val < node

    def __gt__(self, node) -> bool:
        if isinstance(node, Node):
            return self.val > node.val
        return self.val > node

    def __le__(self, node) -> bool:
        if isinstance(node, Node):
            return self.val <= node.val
        return self.val <= node

    def __ge__(self, node) -> bool:
        if isinstance(node, Node):
            return self.val >= node.val
        return self.val >= node


class Tree:
    """Tree data structure
    """
    def __init__(self, root: Node = None):
        self.root = root

    # Tree traversal algorithms
    def inorder_traversal(self, node: Node) -> None:
        """Inorder traversal of the tree - left, parent, right

        Args:
            node (Node): The node to be traversed
        """
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.val, end=", ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node: Node) -> None:
        """Preorder traversal of the tree - parent, left, right

        Args:
            node (Node): The node to be traversed
        """
        if node is not None:
            print(node.val, end=", ")
            self.inorder_traversal(node.left)
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node: Node) -> None:
        """Postorder traversal of the tree - left, right, parent

        Args:
            node (Node): The node to be traversed
        """
        if node is not None:
            self.inorder_traversal(node.left)
            self.inorder_traversal(node.right)
            print(node.val, end=", ")


class BST(Tree):
    """Subclass of Tree class for Binary Search Tree
    """
    def search(self, val: int, node: Node | None) -> bool:
        """_summary_

        Args:
            val (int): _description_
            node (Node): _description_

        Returns:
            bool: _description_
        """
        if node is None:
            return False
        if node.val == val:
            return True
        return self.search(val, node.left) if val < node.val else self.search(val, node.right)

    def insert(self, val: int) -> None:
        """Inserts a value into the BST

        Args:
            val (int): The value to be inserted

        Raises:
            ValueError: If the value is already present in the BST
        """
        new_node = Node(val)
        node = self.root
        if node is None:
            self.root = new_node
            return
        next_node = self.root
        is_left = True
        while next_node is not None:
            if val == node.val:
                raise ValueError(f"Value '{val}' is already in the BST")
            if val > node.val:
                is_left = False
                next_node = node.right
            else:
                is_left = True
                next_node = node.left
            if next_node is not None:
                node = next_node
        if is_left:
            node.left = new_node
        else:
            node.right = new_node


if __name__ == "__main__":
    n1 = Node(4)
    n2 = Node(3)
    n3 = Node(5)
    n4 = Node(1)
    n1.left = n2
    n1.right = n3
    n2.left = n4

    t = Tree(n1)
    print("Inorder Traversal:")
    t.inorder_traversal(t.root)
    print("\nPreorder Traversal:")
    t.preorder_traversal(t.root)
    print("\nPostorder Traversal")
    t.postorder_traversal(t.root)

    n1 = Node(4)
    bst = BST(n1)
    bst.insert(3)
    bst.insert(5)
    bst.insert(1)
    print("\nBST:")
    bst.inorder_traversal(bst.root)

    values = [6,2,4,3,1,5,9,7,8,10]
    bst_2 = BST()
    for value in values:
        bst_2.insert(value)
    print("\nBST 2:")
    bst_2.inorder_traversal(bst_2.root)
