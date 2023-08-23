from Trees.Implement.implementation import TrieNode


def search_word(root: TrieNode, word: str) -> bool:
    curr = root

    for ch in word:
        idx = ord(ch) - ord("a")

        if curr.children[idx] is None:
            return False

        curr = curr.children[idx]

    return curr.eow is True
