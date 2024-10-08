class Solution:
    def minLength(self, s: str) -> int:
        while True:
            len_s = len(s)
            s = s.replace("AB", "")
            s = s.replace("CD", "")
            if len(s) == len_s:
                break
        return len_s

        # stack = []
        # for char in s:
        #     if not stack:
        #         stack.append(char)
        #         continue
        
        #     if char == 'B' and stack[-1] == 'A':
        #         stack.pop()
            
        #     elif char == 'D' and stack[-1] == 'C':
        #         stack.pop()
            
        #     else:
        #         stack.append(char)
        
        # return len(stack)


solution = Solution()

str = "ABFCACDB"
expected = 2

print(solution.minLength(str), '==', expected, ':', str)

str = "ACBBD"
expected = 5

print(solution.minLength(str), '==', expected, ':', str)