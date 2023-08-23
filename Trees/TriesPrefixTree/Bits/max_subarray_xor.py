"""
Given an array of N elements
Find the max value of XOR from all subarrays

Idea 
- here is to create a prefix XOR array
- a pair in the XOR of a pair in prefix XOR array would give you xor of a subarray
- then the problem boils to finding the max XOR pair in XOR prefix array
"""
from Trees.TriesPrefixTree.Bits.max_xor_pair import max_xor_pair


def max_subarray_xor(arr):
    """function"""
    pf_xor = [0] * len(arr)

    pf_xor[0] = arr[0]
    for i in range(1, len(arr)):
        pf_xor[i] = pf_xor[i - 1] ^ arr[i]

    pf_xor.append(0)

    return max_xor_pair(pf_xor)


assert max_subarray_xor([1, 4, 3]) == 7
