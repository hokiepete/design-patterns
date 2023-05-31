class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def traverse_preorder(self):
        # todo - return inorder values (not Nodes)
        return "".join([x for x in self.recursive_preorder()])

    def recursive_preorder(self):
        yield self.value

        if self.left:
            yield self.left.traverse_preorder()

        if self.right:
            yield self.right.traverse_preorder()

node = Node('a',
            Node('b',
                    Node('c'),
                    Node('d')),
            Node('e'))
print(
    'abcde',
    ''.join([x for x in node.traverse_preorder()])
)