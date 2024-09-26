# Завдання про Матриці:
# Дано квадратну матрицю. Напишіть програму, яка повертає матрицю на 90 градусів за годинниковою стрілкою.

# Приклад:
# Вхід:
# 1 2 3
# 4 5 6
# 7 8 9
# Вихід:
# 7 4 1
# 8 5 2
# 9 6 3

massuv = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12],
    [13,14,15],
]

max_x = len(massuv[0])
max_y = len(massuv)

def show_massiv(mass):
    print('-----------')
    for i in mass:
        print(i)

show_massiv(massuv)

result = []

j = 0
for j in range(max_x):
    tmp = []
    for i in reversed(range(max_y)):
        tmp.append(massuv[i][j])
    result.append(tmp)
    j+=1

show_massiv(result)
