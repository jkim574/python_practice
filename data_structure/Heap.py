class BinaryHeap(object):
    def __init__(self):
        self.heap = [0]
        self.currentSize = 0

    def __repr__(self):
        heap = self.heap[1:]
        return ' '.join(str(i) for i in heap)


    # to insert a node in the heap
    def insert(self, key):
        self.heap.append(key)
        self.currentSize += 1
        self.shiftUp(self.currentSize)



    # for finding the child with minimum value
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heap[i * 2] < self.heap[i * 2 + 1]:
                return i * 2
            else:


    # for deleting a node from the heap and maintaining the heap property
    def delete(self):
        deletedNode = self.heap[1]
        self.heap[1] = self.heap[self.currentSize]
        self.currentSize -= 1
        self.heap.pop()
        self.shiftDown(1)
        return deletedNode

    # for building heap
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heap = [0] + alist[:]
        while (i > 0):
            self.shiftDown(i)
            i = i - 1

bh = BinaryHeap()
bh.buildHeap([9,5,6,2,3])

print('Deleted:', bh.delete())
print('Deleted:', bh.delete())
print('Deleted:', bh.delete())
bh.insert(3)
print('Deleted:', bh.delete())
print(bh)
print('Deleted:', bh.)
