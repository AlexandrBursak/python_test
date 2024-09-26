import re
class Solution:
    def myAtoi(self, s: str) -> int:
        dig = re.match(r"^\s*([-+]{0,1}[0-9]+)", s)

        if not dig:
            return 0

        number = int(dig[0])

        if number > (2**31-1):
            return 2**31-1
        if number < (2**31*-1):
            return 2**31*-1

        return number


solution = Solution()
print(solution.myAtoi('1337c0d3'), 1337)
print(solution.myAtoi('-427'), -427)
print(solution.myAtoi('-427'), -427)
print(solution.myAtoi('+427'), 427)
print(solution.myAtoi('    -042'), -42)
print(solution.myAtoi('0-1'), 0)
print(solution.myAtoi("words and 987"), 0)