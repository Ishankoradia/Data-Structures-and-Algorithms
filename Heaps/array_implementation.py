"""
Heap is nothing but a complete binary tree with property 
- Min heap : elements on left > data < elements on right i.e. data is min if we consider the node as root
- Max heap : elements on left <= data >= elements on right i.e. data is max at if we consider the node as root
for all nodes
"""

# here i have implemented a min heap but max heap is very similar too


class Heap:
    def __init__(self, level_order):
        """
        Array representation of a heap is nothing but the level
        order of binary tree that represents the above properties
        """
        self.arr: list = level_order

    def size(self):
        return len(self.arr)

    def heap_property(self, parent, child):
        # min heap property
        # reverse for max heap obviously
        return parent <= child

    def insert(self, k):
        """Insert k in heap"""
        self.arr.append(k)

        # the tree might have lost its property so we need fix it
        i = len(self.arr) - 1
        while i != 0:
            parent = (i - 1) // 2

            if self.heap_property(self.arr[parent], self.arr[i]) is False:
                # swap parent & child
                temp = self.arr[parent]
                self.arr[parent] = self.arr[i]
                self.arr[i] = temp

                i = parent
            else:
                break


level_order_heap = [2, 4, 5, 11, 6, 7, 8, 20, 12]
hp = Heap(level_order=level_order_heap.copy())

hp.insert(3)

assert hp.size() == len(level_order_heap) + 1
assert hp.arr[1] == 3
assert hp.arr[4] == 4
assert hp.arr[9] == 6
