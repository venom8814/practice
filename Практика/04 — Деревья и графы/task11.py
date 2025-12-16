class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = BSTNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_node = self._find_min(node.right)
            node.key = min_node.key
            node.right = self._delete_recursive(node.right, min_node.key)

        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

    def preorder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.key)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.key)

    def is_balanced(self):
        def check_balance(node):
            if node is None:
                return 0, True
            left_height, left_balanced = check_balance(node.left)
            right_height, right_balanced = check_balance(node.right)
            balanced = abs(left_height - right_height) <= 1 and left_balanced and right_balanced
            height = max(left_height, right_height) + 1
            return height, balanced

        _, balanced = check_balance(self.root)
        return balanced


if __name__ == "__main__":
    bst = BST()
    keys = [50, 30, 70, 20, 40, 60, 80]
    for k in keys:
        bst.insert(k)

    print("In-order:", bst.inorder())
    print("Pre-order:", bst.preorder())
    print("Post-order:", bst.postorder())

    print("Поиск 40:", bst.search(40) is not None)
    print("Удаляем 30")
    bst.delete(30)
    print("In-order после удаления:", bst.inorder())

    print("Сбалансировано?", bst.is_balanced())