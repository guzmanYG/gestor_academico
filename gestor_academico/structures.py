class Stack:
    """Pila simple (LIFO) para historial de acciones."""
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop() if self._data else None

    def is_empty(self):
        return len(self._data) == 0

class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BST:
    """Árbol binario de búsqueda simple por clave (ej. matrícula)."""
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = BSTNode(key, value)
            return
        self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key, value)
            else:
                self._insert(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key, value)
            else:
                self._insert(node.right, key, value)
        else:
            node.value = value  # actualizar valor si misma clave

    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return node.value
            node = node.left if key < node.key else node.right
        return None

    def inorder(self):
        result = []
        def _inorder(n):
            if not n:
                return
            _inorder(n.left)
            result.append((n.key, n.value))
            _inorder(n.right)
        _inorder(self.root)
        return result
