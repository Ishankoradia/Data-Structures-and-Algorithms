"""
Super interesting problem that tests your Time complexity skills on arrays and hashmaps
"""

"""
Implement the RandomizedSet class:

- RandomizedSet() Initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into the set if not present. 
Returns true if the item was not present, false otherwise.
- bool remove(int val) Removes an item val from the set if present. 
Returns true if the item was present, false otherwise.
- int getRandom() Returns a random element from the current
set of elements (it's guaranteed that at least one element exists when this method is called). 
Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.
"""

"""
One blog on this would be great
"""

import random


class RandomizedSet:
    def __init__(self):
        self.hm = dict()
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.hm:
            return False

        idx = len(self.arr)
        self.hm[val] = idx
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hm:
            return False

        idx = self.hm[val]
        # swap
        temp = self.arr[idx]
        self.arr[idx] = self.arr[-1]
        self.arr[-1] = temp

        self.hm[temp] = len(self.arr) - 1
        self.hm[self.arr[idx]] = idx

        # remove
        self.arr.pop()
        del self.hm[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
