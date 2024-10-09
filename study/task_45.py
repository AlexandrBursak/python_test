class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack_open = 0
        stack_close = 0

        for el in s:
            if el == '(':
                stack_open += 1
            else:
                if stack_open > 0:
                    stack_open -= 1
                else:
                    stack_close += 1

        return stack_open + stack_close



solution = Solution()

str = "())"
expected = 1

print(solution.minAddToMakeValid(str), '==', expected, ':', str)

str = "((("
expected = 3

print(solution.minAddToMakeValid(str), '==', expected, ':', str)

str = "()))(("
expected = 4

print(solution.minAddToMakeValid(str), '==', expected, ':', str)