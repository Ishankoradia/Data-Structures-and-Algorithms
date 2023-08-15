from Trees.Implement.implementation import TrieNode


def delete_word(root: TrieNode, word: str) -> None:
    curr = root
    temp = root
    next_char = "-"

    for ch in word:
        num_child = 0
        for j in range(26):
            if curr.children[j] is not None:
                num_child += 1

        # node that can't be deleted
        if num_child > 1 or curr.eow is True:
            temp = curr
            next_char = ch

        idx = ord(ch) - ord("a")
        curr = curr.children[idx]

    curr.eow = False

    # check num_child again for the last node
    num_child = 0
    for j in range(26):
        if curr.children[j] is not None:
            num_child += 1

    if num_child <= 1:
        temp.children[ord(next_char) - ord("a")] = None

    return None
