"""
LRU (least recently used)  cache

Design and implement a data structure for Least Recently Used (LRU) cache. 
It should support the following operations: get and set.

    - get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
    - set(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, 
        it should invalidate the least recently used item before inserting the new item.

The LRUCache will be initialized with an integer corresponding to its capacity. 
Capacity indicates the maximum number of unique keys it can hold at a time.

Definition of "least recently used" : An access to an item is defined as a get or a set operation of the item. 
"Least recently used" item is the one with the oldest access time.

NOTE: If you are using any global variables, make sure to clear them in the constructor.
"""

from LinkedList.DoublyLinkedList.implement import ListNode


class ListNodeCache(ListNode):
    def __init__(self, key, value):
        self.data = [key, value]
        self.next = None
        self.prev = None


class LRUCache:
    """Implements lru cache"""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm: dict = dict()  # hashmap to store key values; to have access time O(1)
        self.dummy_head: ListNodeCache = ListNodeCache(-1, -1)
        self.dummy_tail: ListNodeCache = ListNodeCache(-1, -1)

        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    @staticmethod
    def deleteNode(nn: ListNodeCache):
        left: ListNodeCache = nn.prev
        right: ListNodeCache = nn.next

        left.next = right
        right.prev = left

        nn.next = None
        nn.prev = None

        return

    @staticmethod
    def insertNode(nn: ListNodeCache, tail: ListNodeCache):
        left: ListNodeCache = tail.prev
        left.next = nn
        nn.prev = left

        nn.next = tail
        tail.prev = nn

        return

    def set(self, key: int, value: int):
        """set in cache"""

        hm = self.hm

        nn = ListNodeCache(key, value)

        # key exists
        if key in hm:
            nn_to_delete = hm[key]
            # delete the node;
            LRUCache.deleteNode(nn_to_delete)
        else:
            if len(hm) == self.capacity:
                # delete at head; least recently used
                del hm[self.dummy_head.next.data[0]]
                LRUCache.deleteNode(self.dummy_head.next)

        # insert at tail
        LRUCache.insertNode(nn, self.dummy_tail)
        hm[key] = nn

    def get(self, key: int):
        """get from cache"""

        val_node: ListNodeCache = self.hm.get(key, None)

        if val_node:
            temp_node = ListNodeCache(val_node.data[0], val_node.data[1])
            # delete val_node
            LRUCache.deleteNode(val_node)

            # insert temp_node at tail
            LRUCache.insertNode(temp_node, self.dummy_tail)
            self.hm[key] = temp_node

            return temp_node.data[1]

        return -1


# test cases
cache = LRUCache(3)
cache.set(0, 4)  # [[0,4]]
assert cache.get(0) == 4
cache.set(1, 5)  # [[0,4], [1,5]]
cache.set(2, 6)  # [[0,4], [1,5], [2,6]]
assert cache.get(1) == 5  # [[0,4], [2,6], [1,5]]
assert cache.get(2) == 6  # [[0,4], [1,5], [2,6]]
cache.set(3, 7)  # [[0,4], [1,5], [2,6], [3,7]]
cache.set(4, 8)  # [[0,4], [1,5], [2,6], [3,7], [4,8]]
assert cache.get(4) == 8
cache.set(4, 10)  # [[0,4], [1,5], [2,6], [3,7], [4,10]]
assert cache.get(4) == 10
cache.set(11, 20)  # [ [1,5], [2,6], [3,7], [4,10], [11, 20]]
assert cache.get(0) == -1
assert cache.get(11) == 20
cache.set(12, 21)  # [ [2,6], [3,7], [4,10], [11, 20], [12, 21]]
assert cache.get(12) == 21
assert cache.get(2) == -1
