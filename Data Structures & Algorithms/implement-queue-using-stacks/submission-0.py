class MyQueue:

    def __init__(self):
        self.que = []
        

    def push(self, x: int) -> None:
        self.que.append(x)
       

    def pop(self) -> int:
        n = self.que[0]
        del self.que[0]
        return n

    def peek(self) -> int:
        return self.que[0]
        

    def empty(self) -> bool:
        return True if not self.que else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()