class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapper = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for el in s:
            if not stack:
                stack.append(el)
                continue
        
            if el in mapper.values():
                stack.append(el)
            
            elif el in mapper.keys() and stack[-1] == mapper[el]:
                stack.pop()
            
            else:
                stack.append(el)
        
        return len(stack) == 0





solution = Solution()

str = "()"
expected = True

print(solution.isValid(str), '==', expected, ':', str)

str = "()[]{}"
expected = True

print(solution.isValid(str), '==', expected, ':', str)

str = "(]"
expected = False

print(solution.isValid(str), '==', expected, ':', str)

str = "([])"
expected = True

print(solution.isValid(str), '==', expected, ':', str)
        
