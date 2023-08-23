from Trees.Implement.implementation import TrieNode


def insert_word(root: TrieNode, word: str):
    curr: TrieNode = root

    for ch in word:
        idx = ord(ch) - ord("a")

        if curr.children[idx] is None:
            new_trie_node = TrieNode(ch)
            curr.children[idx] = new_trie_node

        curr = curr.children[idx]

    curr.eow = True
