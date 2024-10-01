class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        k = min(len(self.stack), k)
        if k > 0:
            self.stack[:k] = [x+val for x in self.stack[:k]]


tasks =    ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
params =   [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
expected = [None,None,None,2,None,None,None,None,None,103,202,201,-1]

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
            result = operation(*params[i])
        else:
            result = operation()
        # print(i, task, value, result)
        print(i, task, value, result, expected[i])
        assert result == expected[i]