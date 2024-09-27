class Solution:
    def convert(self, s: str, numRows: int) -> str:

        def show_test(m):
            for i in m:
                print(i)
        
        if numRows == 1 or len(s) <= numRows:
            return s

        step = (numRows * 2 - 2)
        P = [''] * numRows 

        # show_test(P)

        row = 0
        block = 0
        for i in range(len(s)):
            if i >= (step + step * block):
                block += 1
                row = 0

            if i < numRows + (step * block):
                row += 1
            else:
                row -= 1

            P[row-1] += s[i]

        return "".join(P)

solution = Solution()
print(solution.convert('ABCDE', 4), 'ABCED')
print(solution.convert('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')
print(solution.convert('PAYPALISHIRING', 4), 'PINALSIGYAHRPI')
print(solution.convert('PAYPALISHIRING', 5), 'PHASIYIRPLIGAN')