from functools import reduce

class Solution:
    def maximumSwap(self, num: int) -> int:
        if num == 0 or num <= 11:
            return num


        list_int = []
        # split the number
        while True:
            list_int.append(num%10)
            if num < 10:
                break
            num = num//10

        i = len(list_int)
        while i > 0:
            # one digit we can't sort
            if i <= 1:
                break
            # find max value in some limit list
            max_value = max(list_int[:i])
            # check if this valu eis n't last in the limit list
            if max_value != list_int[i-1]:
                # sort value between max value and last poss
                list_int[list_int.index(max_value)] = list_int[i-1]
                list_int[i-1] = max_value
                break
            i -= 1

        new_result = reduce(lambda a,b: a*10+b, list_int[::-1])
        return new_result

    # def maximumSwap(self, num: int) -> int:
    #     if num == 0 or num <= 11:
    #         return num

    #     to_list = [int(x) for x in str(num)]

    #     i = 0
    #     while i < len(to_list):
    #         if len(to_list)-i <= 1:
    #             break

    #         max_value = max(to_list[i:])
    #         if int(max_value) != int(to_list[i]):

    #             idx = 0
    #             for pos_i in range(len(to_list)):
    #                 idx = len(to_list) - pos_i - 1
    #                 if max_value == to_list[idx]:
    #                     break

    #             to_list[idx] = to_list[i]
    #             to_list[i] = max_value
    #             break

    #         i += 1

    #     new_result = 0
    #     for num in to_list:
    #         new_result = new_result * 10 + int(num)
    #     return new_result


solution = Solution()

num = 27360
expected = 72360

print(solution.maximumSwap(num), '==', expected, ':', num)

num = 2736
expected = 7236

print(solution.maximumSwap(num), '==', expected, ':', num)

num = 9973
expected = 9973

print(solution.maximumSwap(num), '==', expected, ':', num)

num = 98368
expected = 98863

print(solution.maximumSwap(num), '==', expected, ':', num)

num = 1993
expected = 9913

print(solution.maximumSwap(num), '==', expected, ':', num)