# Завдання про Комбінації:
# Припустимо, у вас є масив цілих чисел і число K. Потрібно знайти всі унікальні комбінації чисел із масиву, сума яких дорівнює K. Кожне число можна використовувати лише один раз у комбінації.

# Приклад:
# Вхід: масив [2, 3, 5, 7], K = 8
# Вихід: [[2, 3, 3], [5, 3], [2, 2, 2, 2]]
# Це завдання перевіряє навички роботи з масивами, рекурсивні функції та вміння ефективно керувати потоком виконання програми.

# import math

masuv = [2, 3, 5, 7, 11]
# 2, 3, 5, 7, 11, 13, 17
k = 8

check = input('Do you want use default (Y/n):')
if check == 'n':
    get_masuv = input('Give the line of number (ex: 1,2,3,4,5):')
    get_k = input('Put the number K (ex: 8): ')

    def modify_masuv(masuv):
        return [int(item) for item in masuv.replace(' ', '').split(',')]
    
    def modify_k(k):
        return int(k.replace(' ', ''))

    masuv = modify_masuv(get_masuv)
    k = modify_k(get_k)

masuv = [item for item in masuv if item < k]

pool = True
masuv_len = len(masuv)

def find_combination(nums, k):
    result = []

    print(nums)

    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                print('continue')
                continue

            if nums[i] > target:
                print('break')
                break

            print('--> Go to loop i, target - nums[i], path + [nums[i]]:', i, target - nums[i], path + [nums[i]])
            backtrack(i, target - nums[i], path + [nums[i]])

    nums.sort()
    backtrack(0, k, [])
    return result


print(masuv, len(masuv))
print(k)
print(find_combination(masuv, k))
