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


class TrieNode:
    def __init__(self, val: str):
        self.val = val
        self.children = [None] * 26
        self.eow = False  # end of word to mark words in the Trie


class TrieBitNode:
    def __init__(self, val: int):
        if val not in [0, 1]:
            raise ValueError("Node values must be binary either 0 or 1")

        self.val = val
        self.children = [None] * 2
