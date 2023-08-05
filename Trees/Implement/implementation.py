class BinaryNode:
    def __init__(self, x) -> None:
        self.val = x
        self.left = None
        self.right = None


class GenericNode:
    def __init__(self, x) -> None:
        self.val = x
        self.children = list()


class Pair:
    def __init__(self, node: BinaryNode, state: int) -> None:
        self.node = node
        self.state = state
