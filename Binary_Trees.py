from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, List, Optional, Tuple, TypeVar

K = TypeVar("K")  # key type (must be comparable)
V = TypeVar("V")  # value type


@dataclass
class _Node(Generic[K, V]):
    key: K
    value: Optional[V] = None
    left: Optional["_Node[K, V]"] = None
    right: Optional["_Node[K, V]"] = None


class BST(Generic[K, V]):
    """
    Binary Search Tree with insert, find, delete and common utilities.
    Keys must be comparable. Values are optional.
    """

    def __init__(self, items: Optional[Iterable[Tuple[K, Optional[V]]]] = None) -> None:
        self._root: Optional[_Node[K, V]] = None
        self._size = 0
        if items:
            for k, v in items:
                self.insert(k, v)

    # ---------- Basic queries ----------

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._root is None

    def contains(self, key: K) -> bool:
        return self._get_node(self._root, key) is not None

    def __contains__(self, key: K) -> bool:  # enables: key in tree
        return self.contains(key)

    def find(self, key: K) -> Optional[V]:
        """Return the value for key, or None if not found (use contains to disambiguate None values)."""
        node = self._get_node(self._root, key)
        return node.value if node else None

    # ---------- Insert / Upsert ----------

    def insert(self, key: K, value: Optional[V] = None) -> None:
        """Insert key (and optional value). If key exists, update its value."""
        self._root, added_new = self._insert(self._root, key, value)
        if added_new:
            self._size += 1

    def _insert(self, node: Optional[_Node[K, V]], key: K, value: Optional[V]) -> Tuple[_Node[K, V], bool]:
        if node is None:
            return _Node(key, value), True
        if key < node.key:
            node.left, added = self._insert(node.left, key, value)
            return node, added
        elif key > node.key:
            node.right, added = self._insert(node.right, key, value)
            return node, added
        else:
            # key exists: update value (not counted as new)
            node.value = value
            return node, False

    # ---------- Delete ----------

    def delete(self, key: K) -> bool:
        """
        Delete key from the tree.
        Returns True if a node was deleted, False if the key wasn't present.
        """
        self._root, deleted = self._delete(self._root, key)
        if deleted:
            self._size -= 1
        return deleted

    def _delete(self, node: Optional[_Node[K, V]], key: K) -> Tuple[Optional[_Node[K, V]], bool]:
        if node is None:
            return None, False

        if key < node.key:
            node.left, deleted = self._delete(node.left, key)
            return node, deleted
        elif key > node.key:
            node.right, deleted = self._delete(node.right, key)
            return node, deleted
        else:
            # Node to delete found
            if node.left is None:
                return node.right, True
            if node.right is None:
                return node.left, True

            # Two children: replace with inorder successor (smallest in right subtree)
            succ = self._min_node(node.right)
            assert succ is not None  # right subtree isn't empty here
            node.key, node.value = succ.key, succ.value
            node.right, _ = self._delete(node.right, succ.key)
            return node, True

    # ---------- Helpers ----------

    def _get_node(self, node: Optional[_Node[K, V]], key: K) -> Optional[_Node[K, V]]:
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node
        return None

    def _min_node(self, node: Optional[_Node[K, V]]) -> Optional[_Node[K, V]]:
        if node is None:
            return None
        while node.left:
            node = node.left
        return node

    def _max_node(self, node: Optional[_Node[K, V]]) -> Optional[_Node[K, V]]:
        if node is None:
            return None
        while node.right:
            node = node.right
        return node

    # ---------- Min/Max ----------

    def min(self) -> Optional[Tuple[K, Optional[V]]]:
        n = self._min_node(self._root)
        return (n.key, n.value) if n else None

    def max(self) -> Optional[Tuple[K, Optional[V]]]:
        n = self._max_node(self._root)
        return (n.key, n.value) if n else None



# ---------------- Demo / quick tests ----------------
if __name__ == "__main__":
    # Build a BST with some keys
    bst = BST[int, str]([(5, "five"), (3, "three"), (8, "eight"), (1, "one"), (4, "four")])

    # Insert / upsert
    bst.insert(7, "seven")
    bst.insert(3, "THREE")  # update value for existing key

    # Queries
    assert 4 in bst and bst.contains(10) is False
    assert bst.find(5) == "five"
    assert bst.min()[0] == 1
    assert bst.max()[0] == 8

    # Delete cases
    bst.delete(1)   # leaf
    bst.delete(3)   # one child (after prior edits)
    bst.delete(5)   # two children (root replacement)
    print("After deletions (inorder):", list(bst.keys()))
    print("Size:", len(bst))
