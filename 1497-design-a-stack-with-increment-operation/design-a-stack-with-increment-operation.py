class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.inc = [0] * maxSize
        self.values = -1
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if self.values == self.maxSize - 1:
            return
        self.values += 1
        self.stack[self.values] = x

    def pop(self) -> int:
        if self.values == -1:
            return -1
        result = self.stack[self.values] + self.inc[self.values]

        if self.values > 0:
            self.inc[self.values - 1] += self.inc[self.values]

        self.inc[self.values] = 0
        self.values -= 1
        return result
    
    def increment(self, k: int, val: int) -> None:
        index = min(k-1, self.values)
        if index >= 0:
            self.inc[index] += val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)