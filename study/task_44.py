class Solution:
    def minSwaps(self, s: str) -> int:

        # doesn't work
        # correct = 0

        # idx = 1
        # while idx < len(s):

        #     back_loop = True
        #     back_idx = 0
        #     while back_loop:
        #         if s[idx + back_idx] != s[idx - 1 - back_idx] and s[idx - 1 - back_idx] == '[':
        #             correct += 2
        #             idx += 1
        #         back_loop = False

        #     idx += 1

        # len_s = len(s) - correct
        # if len_s == 0:
        #     return 0
        # if len_s == 2:
        #     return 1
        # if len_s%4:
        #     return int(len_s/4) + 1
        # return int(len_s/4)


        # works
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            elif i != stack[-1] and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)

        if len(stack) == 0:
            return 0
        if len(stack) == 2:
            return 1

        return int((len(stack)+2)//4)
    
        # is not my algo
        # stack_idx = 0
        # for el in s:
        #     if el == '[':
        #         stack_idx += 1
        #     else:
        #         if stack_idx > 0:
        #             stack_idx -= 1
        # return (stack_idx + 1) // 2


solution = Solution()

str = "][]["
expected = 1

print(solution.minSwaps(str), '==', expected, ':', str)

str = "]]][[["
expected = 2

print(solution.minSwaps(str), '==', expected, ':', str)

str = "[]"
expected = 0

print(solution.minSwaps(str), '==', expected, ':', str)

str = "[[][[[[][][[[[]]][][]]]]][[][[][][]][[[[]]][[]][[]][[]]]]]]]][]][]]][[]][[[[[[][[]][[[][]][[]]]["
expected = 3

print(solution.minSwaps(str), '==', expected, ':', str)

str = "[[][[[]]]]"
expected = 0

print(solution.minSwaps(str), '==', expected, ':', str)