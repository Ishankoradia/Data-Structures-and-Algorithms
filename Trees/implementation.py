class BinaryNode:
    def __init__(self, x) -> None:
        self.val = x
        self.left = None
        self.right = None


class GenericNode:
    def __init__(self, x) -> None:
        self.val = x
        self.children = list()
