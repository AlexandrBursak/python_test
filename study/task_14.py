class Solution:

    def longestPalindrome(self, s: str) -> str:
        ts = '#'.join(f'-{s}+')
        n = len(ts)
        P = [0] * n

        for i in range(1, n - 1):
            while ts[i - P[i] - 1] == ts[i + P[i] + 1]:
                P[i] += 1

        max_len = max(P)
        center_index = P.index(max_len)

        start = (center_index - max_len) // 2
        return s[start:start+max_len]

        

    # def longestPalindrome(self, s: str) -> str:
    #     poli = {}
    #     max_poli = 0
    #     length_s = len(s)
    #     for i in range(length_s+1):
    #         for j in range(i+1):
    #             if i - j < max_poli:
    #                 break
    #             test_str = s[j:i]
    #             if test_str == test_str[::-1]:
    #                 len_test_str = len(test_str)
    #                 if len_test_str > max_poli:
    #                     poli[len_test_str] = test_str
    #                     max_poli = len_test_str
    #                 break

    #     return poli[max_poli]

    # def longestPalindrome(self, s: str) -> str:
    #     poli = {1: s[0]}
    #     max_poli = 1
    #     length_s = len(s)
    #     for i in range(len(s)):
    #         for j in range(len(s[i:])):
    #             right = length_s - j
    #             temp_s = s[i:right]
    #             length = len(temp_s)

    #             if length < max_poli:
    #                 break

    #             # print('temp_s, temp_s[::-1] =', temp_s, temp_s[::-1], length)

    #             if temp_s == temp_s[::-1]:
    #                 if len(temp_s) not in poli.keys():
    #                     poli[len(temp_s)] = temp_s
    #                     max_poli = max(max(poli.keys()), max_poli)
    #                 break
                
    #             if length <= 2:
    #                 break

    #     print(poli)
    #     return poli[max_poli]


solution = Solution()
print(solution.longestPalindrome('babaddtattarrattatddetartrateedredividerb'))
print(solution.longestPalindrome('babad'))
print(solution.longestPalindrome('abb'))
