from collections import deque 

class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = deque()
        self.maxSize = k
        self.value = -1

    def insertFront(self, value: int) -> bool:
        if self.value < self.maxSize-1:
            self.queue.appendleft(value)
            self.value += 1
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        if self.value < self.maxSize-1:
            self.queue.append(value)
            self.value += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.value > -1:
            self.queue.popleft()
            self.value -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.value > -1:
            self.queue.pop()
            self.value -= 1
            return True
        return False      

    def getFront(self) -> int:
        return self.queue[0] if self.value > -1 else -1
            
    def getRear(self) -> int:
        return self.queue[-1] if self.value > -1 else -1

    def isEmpty(self) -> bool:
        if self.value == -1:
            return True
        return False
        
    def isFull(self) -> bool:
        if self.value == self.maxSize-1:
            return True
        return False
        

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()