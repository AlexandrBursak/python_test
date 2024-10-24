def yield_items(iterable):
    for i in iterable:
        yield i
        
zero_two = iter([0, 1, 2])

assert list(yield_items(zero_two)) == [0,1,2]
assert list(yield_items(zero_two)) == []

print('yep')

# from functools import wraps

# def incrimentor(func):
#     a = 0
    
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         nonlocal a
#         a += 1
#         return func(*args, **kwargs) + a
    
#     return wrapper


# @incrimentor
# def plus(a, b):
#     return a + b

# @incrimentor
# def minus(a, b):
#     return a - b


# assert plus(1, 1) ==  3
# assert plus(1, 1) + minus(1, 1) == 5

# print('yup')

# class A:
#     field_1 = 42
#     field_2 = -42
    
#     def __init__(self, field_1: int=None, field_2: int=None):
#         if field_1 is not None:
#             self.field_1 = field_1
#         if field_2 is not None:
#             self.field_2 = field_2


# a = A(1)

# A.field_1 = 10
# A.field_2 = 20

# assert a.field_1 == 1
# assert a.field_2 == 20

# print('kk')

from io import BytesIO

import pandas as pd


csv_content = BytesIO(b"""temp,time,date
1,0:00,24.04.2024
0,6:00,24.04.2024
8,12:00,24.04.2024
4,18:00,24.04.2024
2,0:00,25.04.2024
-1,6:00,25.04.2024
5,12:00,25.04.2024
3,18:00,25.04.2024
5,0:00,26.04.2024
0,6:00,26.04.2024
10,12:00,26.04.2024
6,18:00,26.04.2024
""")

df = pd.read_csv(csv_content)

print('#### 1. Please, display all records for 25.04.2024')
for index, row in df.iterrows():
    if row.date == '25.04.2024':
        print(row)

print('#### 2. Please, display all records with the temperature above 5 degrees at 12:00')
for index, row in df.iterrows():
    if row.time == '12:00' and row.temp > 5:
        print(row)

print('#### 3. Let\'s say it\'s a database table (e.g. MySQL) not a csv file. Please, write an SQL query to get dates with average temperature above 4 degrees.')
sql = "SELECT date FROM temperatures GROUP by date HAVING AVG(temp) > 4"