class PowTwo:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self
    
    def __next__ (self):
        if self.n <= self.max:
            res = 2 ** self.n
            self.n += 1
            return res
        else:
            raise StopIteration
        
    
if __name__ == "__main__":
    numbers = PowTwo(3)
    it = iter(numbers)

    print(next(it))
    print(next(it))
    print(next(it))