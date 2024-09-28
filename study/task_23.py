from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = ''
        try:
            for i, letter in enumerate(strs[0]):
                for j in range(1, len(strs)):
                    if i >= len(strs[j]) or letter != strs[j][i]:
                        raise Exception
                prefix += letter
        except Exception:
            pass

        return prefix

        

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]), 'fl')
print(solution.longestCommonPrefix(["ab", "a"]), 'a')
