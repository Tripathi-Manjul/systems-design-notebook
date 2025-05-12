"""
B-Tree Implementation (Simplified) – For Learning Indexing Concepts

Connection to Kleppmann:
- B-trees support ordered, log-time lookups → critical for relational joins and range queries.
- Nodes keep keys sorted → ideal for SQL ORDER BY, BETWEEN, cursor-based pagination.
"""

class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []        # Sorted list of keys
        self.children = []    # Pointers to child nodes

class BTree:
    def __init__(self, degree=2):  # Minimum degree (t): max keys = 2*t - 1
        self.root = BTreeNode(leaf=True)
        self.degree = degree

    def search(self, key, node=None):
        """
        Recursive search for a key in the B-tree.

        Time complexity: O(log n)
        """
        if node is None:
            node = self.root

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return True

        if node.leaf:
            return False

        return self.search(key, node.children[i])

    def insert(self, key):
        """
        Inserts a key into the B-tree.
        Splits the root if needed.
        """
        root = self.root
        if len(root.keys) == (2 * self.degree - 1):
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root

        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1

        if node.leaf:
            node.keys.append(None)  # Placeholder
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            if len(node.children[i].keys) == (2 * self.degree - 1):
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent, i):
        t = self.degree
        node_to_split = parent.children[i]
        new_node = BTreeNode(leaf=node_to_split.leaf)

        # Median key moves up
        parent.keys.insert(i, node_to_split.keys[t - 1])
        parent.children.insert(i + 1, new_node)

        # Split keys and children
        new_node.keys = node_to_split.keys[t:(2 * t - 1)]
        node_to_split.keys = node_to_split.keys[0:t - 1]

        if not node_to_split.leaf:
            new_node.children = node_to_split.children[t:(2 * t)]
            node_to_split.children = node_to_split.children[0:t]

# Demo
if __name__ == "__main__":
    tree = BTree(degree=2)
    for key in [10, 20, 5, 6, 12, 30, 7, 17]:
        tree.insert(key)

    print("Search 6:", tree.search(6))   # True
    print("Search 15:", tree.search(15)) # False
