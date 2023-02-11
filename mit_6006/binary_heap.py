
class MaxHeap:
    '''Requirements:
    - insert - O(log(N))
    - find_max - O(1)
    - delete_max O(log(N))
    '''
    def __init__(self):
        self.arr = []
        self.size = 0

    def _swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def find_max(self, ):
        if self.size > 0:
            return self.arr[0]
        
    def insert(self, key):
        self.arr.append(key)
        self.size += 1
        self.max_heapify_up(self.size-1)

    def delete_max(self, ):
        if self.size <= 0: return
        self._swap(0, self.size-1)
        max_elem = self.arr.pop()
        self.size -= 1
        self.max_heapify_down(0)
        return max_elem

    def _left(self, i):
        return 2*i + 1
            
    def _right(self, i):
        return 2*i + 2

    def _key(self, i):
        if i < self.size:
            return self.arr[i]

    def _parent(self, i):
        return int((i - 1) / 2)
    
    def max_heapify_up(self, i):
        p = self._parent(i)
        if p == i == 0:
            return 
        if self._key(p) < self._key(i):
            self._swap(p, i)
            self.max_heapify_up(p)
    
    def max_heapify_down(self, i):
        l, r = self._left(i), self._right(i)
        mx = max([i, l, r], key=lambda k: (self._key(k) or -float('inf')))
        
        if mx != i:
            self._swap(i, mx)
            self.max_heapify_down(mx)

    @classmethod
    def linear_build(cls, arr, inplace=False):
        self = cls()
        self.arr = arr[:] if not inplace else arr
        self.size = len(arr)
        for i in range(self.size - 1, -1, -1):
            self.max_heapify_down(i)
        return self 

    def is_valid_mx_heap(self,):
        for i in range(self.size):
            l, r = self._left(i), self._right(i)
            mx = max([i, l, r], key=lambda x: (self._key(x) or -float('inf')))
            if mx != i:
                return False 
        return True 
    

def heapsort(arr):
    mx_heap = MaxHeap.linear_build(arr)
    print('Is valid max heap build?', mx_heap.is_valid_mx_heap())
    n = mx_heap.size
    arr = []
    for _ in range(n):      # n
        x = mx_heap.delete_max()  # O(logN)
        arr.append(x)  # O(1)
    return arr[::-1]

def inplace_heapsort(arr):
    mx_heap = MaxHeap.linear_build(arr, inplace=True)
    n = mx_heap.size
    for _ in range(n):
        mx = mx_heap.delete_max()
        mx_heap.arr.append(mx)
    

        





def test_maxheap():
    import random, copy 
    
    arr = [random.randint(0, 20) for i in range(20)]
    # arr = [3, 14, 0, 7, 12, 5, 2, 4, 5, 10, 14, 12, 17, 19, 0, 4, 14, 19, 2, 20]

    print(arr)
    mx_heap = MaxHeap()

    for a in arr[:10]:
        mx_heap.insert(a)
        # print('current_max:', mx_heap.find_max())
    
    print('max:', mx_heap.find_max())
    for _ in range(5):
        print('deleted:', mx_heap.delete_max())

    for a in arr[10:]:
        mx_heap.insert(a)
        # print('current_max:', mx_heap.find_max())

    print('arr:', mx_heap.arr)
    print('heap sorted:', heapsort(arr))
    print('sorted:', sorted(arr))
    _arr = copy.deepcopy(arr)
    inplace_heapsort(_arr)
    print('inplace_sorted:', _arr)


    

test_maxheap()
