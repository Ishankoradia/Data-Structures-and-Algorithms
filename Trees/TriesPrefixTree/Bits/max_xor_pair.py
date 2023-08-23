"""
Given an array of N elements
Find the max value of XOR pair i.e. A[i] ^ A[j] should be maximum
where i, j in (0, N-1) 
"""
from Trees.Implement.implementation import TrieBitNode
from Trees.TriesPrefixTree.Bits.build_bit_trie import build_bit_trie


def max_xor_pair(arr) -> int:
    """Function"""

    root, max_bit_cnt = build_bit_trie(arr)

    max_xor = 0
    for num in arr:
        curr = root
        # try to find the best pair for this num that will max XOR val
        # idea is to find the number with opposite MSB bits
        xor = 0
        for i in range(max_bit_cnt - 1, -1, -1):
            curr_bit = num >> i & 1

            # ith bit in num is set
            if curr_bit == 1:
                if curr.children[0] is not None:
                    xor = xor | (1 << i)
                    curr = curr.children[0]
                else:
                    curr = curr.children[1]
            else:
                if curr.children[1] is not None:
                    xor = xor | (1 << i)
                    curr = curr.children[1]
                else:
                    curr = curr.children[0]

        max_xor = max(xor, max_xor)

    return max_xor


assert max_xor_pair([9, 8, 10, 7]) == 15
