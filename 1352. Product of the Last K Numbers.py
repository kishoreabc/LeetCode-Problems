class ProductOfNumbers:

    def __init__(self):
        self.lst = []

    def add(self, num: int) -> None:
        self.lst.append(num)
        self.store = dict()
    def getProduct(self, k: int) -> int:
        if len(self.lst)<1:
            return stack
        result = 1
        if k in self.store:
            return self.store[k][1]
        for i in range(1,k+1):
            result *= self.lst[-i]
        self.store[k] = (len(self.lst),result)
        return result


        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
