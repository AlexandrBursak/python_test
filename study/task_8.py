class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dummy = []

        count = 0
        for alph in s:
            if alph in dummy:
                dummy = dummy[dummy.index(alph)+1:]
                count = max(len(dummy), count)
            dummy.append(alph)
            count = max(len(dummy), count)
        
        return count


solution = Solution()
print(solution.lengthOfLongestSubstring('abcabcbb'))
print(solution.lengthOfLongestSubstring('bbbbb'))
print(solution.lengthOfLongestSubstring('pwwkew'))
print(solution.lengthOfLongestSubstring(' '))
print(solution.lengthOfLongestSubstring('dvdf'))
