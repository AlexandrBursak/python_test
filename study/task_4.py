# Завдання: Паліндроми в Списку
# Припустимо, у нас є пов'язаний список, і наше завдання - визначити, чи він є паліндромом. Паліндром - це послідовність, яка читається однаково вперед і назад.

import math

string = 'ab5fttf5ba'

print(string)
print(len(string))

def is_polyndrom():
    return str(string) == str(string)[::-1]

if is_polyndrom():
    print('This is a polyndrom')
else:
    print('This is not a polyndrom')