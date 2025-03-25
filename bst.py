class Node:
    """Class representing a node in a binary search tree"""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    """Binary Search Tree implementation"""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a new key into the BST"""
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)
        return node

    def search(self, key):
        """Search for a key in the BST"""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        """Perform inorder traversal of the BST (sorted order)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

# Example usage
if __name__ == "__main__":
    bst = BST()
    elements = [50, 30, 70, 20, 40, 60, 80]
    for elem in elements:
        bst.insert(elem)

    print("Inorder Traversal:", bst.inorder_traversal())  # Should print sorted elements

    # Search for a node
    key = 40
    if bst.search(key):
        print(f"Key {key} found in BST")
    else:
        print(f"Key {key} not found in BST")
