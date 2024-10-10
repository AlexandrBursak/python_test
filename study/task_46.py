from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def isValid(s) -> bool:
            open_br = 0
            for el in s:
                if el == '0':
                    open_br += 1
                else:
                    if open_br == 0:
                        return False
                    else:
                        open_br -= 1
            return open_br == 0

        res_list = []
        measure = int(2**(n+n))
        for i in range(1, measure, 2):
            s = "{0:{fill}{width}b}".format(i, fill='0', width = n*2)
            if s[0] != '1' and isValid(s):
                res = s.replace('0', '(')
                res = res.replace('1', ')')
                res_list.append(res)
        
        return res_list

solution = Solution()

str = 3
expected = ["((()))","(()())","(())()","()(())","()()()"]

print(solution.generateParenthesis(str), '==', expected, ':', str)

str = 1
expected = ["()"]

print(solution.generateParenthesis(str), '==', expected, ':', str)

str = 0
expected = []

print(solution.generateParenthesis(str), '==', expected, ':', str)

str = 2
expected = ["(())","()()"]

print(solution.generateParenthesis(str), '==', expected, ':', str)

# str = 4
# expected = ["(())","()()"]

# print(solution.generateParenthesis(str), '==', expected, ':', str)

# str = "()))(("
# expected = 4

# print(solution.generateParenthesis(str), '==', expected, ':', str)