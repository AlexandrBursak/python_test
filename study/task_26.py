class Node:
    def __init__(self):
        self.value = []
        self.count = []
        self.last_max = ''
        self.last_min = ''

class AllOne:

    def __init__(self):
        self.k_node = Node()

    def inc(self, key: str) -> None:
        if key in self.k_node.value:
            self.k_node.count[self.k_node.value.index(key)] += 1
        else:
            self.k_node.count.append(1)
            self.k_node.value.append(key)
        
        self.k_node.last_max = ''
        self.k_node.last_min = ''

    def dec(self, key: str) -> None:
        if key in self.k_node.value:
            if self.k_node.count[self.k_node.value.index(key)] == 1:
                del self.k_node.count[self.k_node.value.index(key)]
                del self.k_node.value[self.k_node.value.index(key)]
            else: 
                self.k_node.count[self.k_node.value.index(key)] -= 1
            self.k_node.last_max = ''
            self.k_node.last_min = ''

    def getMaxKey(self) -> str:
        if self.k_node.value:
            if self.k_node.last_max == '':
                self.k_node.last_max = self.k_node.value[self.k_node.count.index(max(self.k_node.count))]
            return self.k_node.last_max
        return ''
        
    def getMinKey(self) -> str:
        if self.k_node.value:
            if self.k_node.last_min == '':
                self.k_node.last_min = self.k_node.value[self.k_node.count.index(min(self.k_node.count))]
            return self.k_node.last_min
        return ''


# tasks = ["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"]
# params = [[],["hello"],["hello"],[],[],["leet"],[],[]]
# expected = [None, None, None, "hello", "hello", None, "hello", "leet"]

tasks =    ["AllOne","inc",    "inc",      "inc",    "inc",    "getMaxKey","inc",   "inc",   "inc",   "dec",    "inc",   "inc",   "inc",   "getMaxKey"]
params =   [[],      ["hello"],["goodbye"],["hello"],["hello"],[],         ["leet"],["code"],["leet"],["hello"],["leet"],["code"],["code"],[]]
expected = [None,    None,     None,       None,     None,     "hello",    None,    None,    None,    None,     None,    None,    None,    "leet"]

# tasks =    ["AllOne","inc","inc","inc","inc","inc","inc","inc","inc","inc","inc","inc","inc","getMinKey"]
# params =   [[],["a"],["b"],["c"],["d"],["a"],["b"],["c"],["d"],["c"],["d"],["d"],["a"],[]]
# expected = [None,None,None,None,None,None,None,None,None,None,None,None,None,"b"]

# tasks =    ["AllOne","inc","inc","inc","inc","inc","inc","dec", "dec","getMinKey","dec","getMaxKey","getMinKey"]
# params =   [[],["a"],["b"],["b"],["c"],["c"],["c"],["b"],["b"],[],["a"],[],[]]
# expected = [None,None,None,None,None,None,None,None,None,None,None,None,None,"b"]

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
        # print(i, task, value, result)
        print(i, task, value, result, expected[i])
        assert result == expected[i]
