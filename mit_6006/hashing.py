from dynamic_array import DArray
import random
class HashTable:
    def __init__(self, m=5):
        self.p = 2**16+1
        self.a = random.randint(1, self.p-1)
        self.m = m
        self.store = [DArray() for _ in range(self.m)]

    
    def _hash(self, x):
        return ((self.a*x) % self.p ) % self.m
    

    def insert(self, x):
        hash_val = self._hash(x)
        for v in self.store[hash_val]:
            if v == x:
                return 
        self.store[hash_val].append(x)
    
    def _unorder_remove(self, darray, i):
        if not (i == darray.len - 1):
            last = darray.len - 1
            arr = darray.arr 
            arr[last], arr[i] = arr[i], arr[last]
        return darray.pop()
        

    def delete(self, x):
        (hash_val, i) = self.find(x)
        if i is not None:
            hash_val = self._hash(x)
            self._unorder_remove(self.store[hash_val], i)
        
    
    def find(self, x):
        hash_val = self._hash(x)
        for i, v in enumerate(self.store[hash_val]):
            if v == x:
                return (hash_val, i)
        return None, None

    
    def __len__(self):
        return sum([darray.len for darray in self.store])
    
    def __str__(self):
        return str([str(i) + ': ' + str(d) for i, d in enumerate(self.store) if d.len > 0])

    def __iter__(self):
        for s in self.store:
            for v in s:
                yield v 



def test():
    array = [random.randint(0, 1000) for i in range(20)]

    hash_table = HashTable()
    for i, a in enumerate(array):
        hash_table.insert(a)
        if i%5 == 0:
            print(hash_table)
    to_remove = random.choices(array, k=5)
    print(to_remove, 'to remove')
    for r in to_remove:
        hash_table.delete(r)
    
    to_remove = random.choices(array, k=5)
    print(to_remove, 'to find')
    for r in to_remove:
        print(hash_table.find(r))

    print('iter')
    print(hash_table)
    for i in hash_table:
        print(i, end=' ')


if __name__ == '__main__':

    test()
    
    

