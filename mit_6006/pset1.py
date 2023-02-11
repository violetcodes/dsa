
class DE_Dynamic_Array:
    def __init__(self, s=1):
        self.array = [None for _ in range(s)]
        self.size = s 
        self.zero = 0
        self.last = 0
        self.first = 0

    def get_at(self, i):
        if self.first + i <= self.last:
            yield self.array[self.first + i]

    def set_at(self, i, x):
        if self.first + i <= self.last:
            self.array[self.first + i] = x


    def insert_first(self, val):
        if self.first - 1 >= 0:
            self.first -= 1
            self.set_at()
        
        else: 
            self.first += self.len() 
            self.array = [None] * self.first + self.array 
            self.insert_first(val)
        
    
    
        
        