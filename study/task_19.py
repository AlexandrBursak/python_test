import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # loop = True
        # i = 0
        # while loop:
        for i in range(len(p)):

            print(p[i])
            if i == 0:


                
            if p[i] not in ['.', '*']:




            # if i < 10:
            #     loop = False
            #     i += 1
            # if bad:
                # return False


    # def isMatch(self, s: str, p: str) -> bool:
    #     pattern = rf'^({p})$'

    #     print('pattern',pattern)
    #     res = re.match(pattern, s)

    #     print('res:', res)

    #     # print('extraSplution', self.extraSplution(s, p))
    #     return True if res and res[0] else False 

solution = Solution()
print(solution.isMatch("aab", "c*a*b"), True)
# print(solution.isMatch('aaraaraar', 'aar*'), True)
# print(solution.isMatch('abas', 'aba.'), True)
# print(solution.isMatch('aa', 'a*'), True)
# print(solution.isMatch('ab', '.*'), True)