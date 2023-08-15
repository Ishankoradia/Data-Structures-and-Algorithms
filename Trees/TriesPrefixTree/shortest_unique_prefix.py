"""
For example the set of words
{tri, trap, plate, cat, part, place, tie}

will have the shortest unique prefixes as

{tri, tra, plat, c, pa, plac, ti}

assume no word is prefix of another word
"""
from Trees.Implement.implementation import TrieNode


class PrefixTrieNode(TrieNode):
    def __init__(self, val):
        super().__init__(val)
        self.count = 1


def build_prefix_tree(words: list[str]):
    root = PrefixTrieNode("#")

    for word in words:
        curr = root
        for ch in word:
            idx = ord(ch) - ord("a")
            if curr.children[idx] is None:
                curr.children[idx] = PrefixTrieNode(ch)
            else:
                curr.children[idx].count += 1

            curr = curr.children[idx]

    return root


def search_unique_prefix(words: list[str]):
    root = build_prefix_tree(words)

    ans = []

    for word in words:
        curr = root
        i = 0
        while i < len(word):
            idx = ord(word[i]) - ord("a")
            i += 1
            if curr.children[idx].count == 1:
                break
            else:
                curr = curr.children[idx]

        ans.append(word[0:i])

    return ans


assert search_unique_prefix(
    ["tri", "trap", "plate", "cat", "part", "place", "tie"]
) == ["tri", "tra", "plat", "c", "pa", "plac", "ti"]
