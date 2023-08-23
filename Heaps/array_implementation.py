"""
Heap is nothing but a complete binary tree with property 
- Min heap : elements on left > data < elements on right i.e. data is min if we consider the node as root
- Max heap : elements on left <= data >= elements on right i.e. data is max at if we consider the node as root
for all nodes
"""

# here i have implemented a min heap but max heap is very similar too


class Heap:
    def __init__(self, arr: list):
        """
        Array representation of a heap is nothing but the level
        order of binary tree that represents the above properties
        """
        self.arr: list = Heap.heapfiy(arr)

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

    @classmethod
    def heapfiy(cls, arr1: list):
        """Transform the array into a heap with the min heap property"""

        # consider the arr as the level order of a complete binary tree that does not yet have a heap property
        # all the leaf nodes already satisfy the heap property so we need from the parent of last element
        last_idx = len(arr1) - 1

        parent_last = (last_idx - 1) // 2

        for i in range(parent_last, -1, -1):
            Heap.downheapify(arr1, i)

        return arr1

    @classmethod
    def downheapify(cls, heap: list, root_idx: int) -> None:
        """Heapify the heap from ith ele to the last level with leaf nodes"""
        n = len(heap)
        while 2 * root_idx + 1 < n:
            left_idx = 2 * root_idx + 1
            right_idx = 2 * root_idx + 2
            min_val = min([heap[root_idx], heap[left_idx], heap[right_idx]])

            if min_val == heap[root_idx]:
                break
            elif min_val == heap[left_idx]:
                # swap root,left
                temp = heap[root_idx]
                heap[root_idx] = heap[left_idx]
                heap[left_idx] = temp

                root_idx = left_idx
            else:
                # swap root,right
                temp = heap[root_idx]
                heap[root_idx] = heap[right_idx]
                heap[right_idx] = temp

                root_idx = right_idx

        return None


# you can pass any array, our class will heapify and create a valid min heap
arr = [20, 12, 11, 7, 8, 6, 2, 4, 5]

hp = Heap(arr.copy())
assert hp.arr == [2, 4, 6, 5, 8, 20, 11, 7, 12]

hp.insert(3)

assert hp.size() == len(arr) + 1
assert hp.arr[1] == 3
assert hp.arr[4] == 4
