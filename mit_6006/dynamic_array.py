class DArray:
    def __init__(self, size=2):
        self.arr = [None for _ in range(size)]
        self.len = 0
        self.size = size 

    def __iter__(self, ):
        for i in range(self.len):
            yield self.arr[i]
    
    def append(self, x):
        if self.len < self.size:
            self.arr[self.len] = x
            self.len += 1
        else:
            self.double_arr()
            self.append(x)

    def pop(self):
        if self.len == 0: return 
        x = self.arr[self.len-1]
        self.arr[self.len-1] = None 
        self.len -= 1
        if self.len <= self.size // 2:
            self.size = self.size // 2
            self.arr = self.arr[:self.size]
        return x 

    def double_arr(self):
        self.arr += [None] * self.size 
        self.size *= 2 


    def __str__(self,):
        return str(self.arr[:self.len])
    
    def __len__(self,):
        return self.len
    


def test_darray():
    import random 
    array = [random.randint(0, 1000) for i in range(20)]

    darray = DArray()
    for a in array:
        darray.append(a)
        print(darray, darray.size)
    
    for _ in range(10):
        a = darray.pop()
        print(a, darray, darray.size)

if __name__ == '__main__':
    test_darray()

        

        