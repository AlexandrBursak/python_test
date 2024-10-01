class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.deque = []

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.deque.insert(0, value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.deque.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            del self.deque[0]
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            del self.deque[-1]
            return True
        else:
            return False

    def getFront(self) -> int:
        try:
            return self.deque[0]
        except:
            return -1

    def getRear(self) -> int:
        try:
            return self.deque[-1]
        except:
            return -1

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) == self.k


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


# Your MyCircularDeque object will be instantiated and called as such:

tasks = ["MyCircularDeque","insertLast","insertLast","insertFront","insertFront","getRear","isFull","deleteLast","insertFront","getFront"]
params = [[3],[1],[2],[3],[4],[],[],[],[4],[]]
expected = [None,True,True,True,False,2,True,True,True,4]

obj = None
for i, task in enumerate(tasks):
    if len(params[i]):
        value = params[i][0]
    else: 
        value = None
    if i == 0:
        define_task = globals()[task]
        if value:
            obj = define_task(value)
        else:
            obj = define_task()
    else:
        operation = getattr(obj, task)
        if value:
            result = operation(value)
        else:
            result = operation()
        print(i, result, expected[i])
        assert result == expected[i]


# myCircularDeque = MyCircularDeque(3)
# print(myCircularDeque.insertLast(1));  # return True
# print(myCircularDeque.insertLast(2));  # return True
# print(myCircularDeque.insertFront(3)); # return True
# print(myCircularDeque.insertFront(4)); # return False, the queue is full.
# print(myCircularDeque.getRear());      # return 2
# print(myCircularDeque.isFull());       # return True
# print(myCircularDeque.deleteLast());   # return True
# print(myCircularDeque.insertFront(4)); # return True
# print(myCircularDeque.getFront());     # return 4