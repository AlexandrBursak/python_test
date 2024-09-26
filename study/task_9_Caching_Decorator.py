from functools import wraps

def cached(func):
    cached_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        # x, y, z = args
        hash_of_dict = (args, frozenset(kwargs.items()))
        print('kwargs.items()', kwargs.items())
        print('hash_of_dict', hash_of_dict)
        if hash_of_dict not in cached_dict:
            print('get result and save to cache')
            cached_dict[hash_of_dict] = func(*args, **kwargs)
        
        print('get from cache')
        return cached_dict[hash_of_dict]

    return wrapper

@cached 
def do_something(x, y, z, r = None): 
    return x + y * z 

print('Check 1')
assert do_something(1, 2, 3, r=5) == 7 
print('Check 2')
assert do_something(1, 2, 3) == 7 # result from cache 


# def cache_decorator(func):
#     cache = {}
    
#     # @wraps(func)
#     def wrapper(*args, **kwargs):
#         # Створюємо ключ для кеша з аргументів функції/методу
#         key = (args, frozenset(kwargs.items()))
#         print('key:', key)
        
#         if key not in cache:
#             # Обчислюємо результат та зберігаємо його в кеш
#             print('Зберігаємо в кеш')
#             cache[key] = func(*args, **kwargs)
        
#         print('Вертаємо результат з кешу')
#         print('Show cache', cache)
#         return cache[key]
    
#     return wrapper

@cached
def add(a, b):
    print(f"Calculating {a} + {b}")
    return a + b

# Викликаємо функцію кілька разів
print(add(4, 3))  # Обчислюється вперше
print(add(4, 3))  # Використовується кешований результат
print(add(5, 6))  # Обчислюється вперше

@cached
def minus(a, b):
    print(f"Calculating {a} - {b}")
    return a - b

print(minus(4, 3))  # Обчислюється вперше
print(minus(4, 3))  # Використовується кешований результат

class Calculator:
    
    @cached
    def multiply(self, x, y):
        print(f"Calculating {x} * {y}")
        return x * y

calc = Calculator()
print(calc.multiply(3, 4))  # Обчислюється вперше
print(calc.multiply(3, 4))  # Використовується кешований результат
print(calc.multiply(5, 6))  # Обчислюється вперше