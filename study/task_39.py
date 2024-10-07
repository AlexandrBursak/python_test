class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False
        
        s1_sorted = sorted(s1)

        for i in range(s2_len+1-s1_len):
            if sorted(s2[i:i+s1_len]) == s1_sorted:
                return True
        return False

    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     s1_len = len(s1)
    #     s2_len = len(s2)
    #     if s1_len > s2_len:
    #         return False

    #     for i in range(s2_len+1-s1_len):
    #         s2[i:i+s1_len]
    #         for j in s1:
    #             if j not in s2[i:i+s1_len]:
    #                 break
    #         else:
    #             return True
    #     return False

    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     # alph = 'abcdefghijklmnopqrstuvwxz'
    #     alph = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}
    #     s1_len = len(s1)
    #     s2_len = len(s2)
    #     if s1_len > s2_len:
    #         return False

    #     sum_alpha = 0
    #     for i in s1:
    #         sum_alpha += alph[i]
        
    #     for i in range(s2_len+1-s1_len):
    #         check_alpha = 0
    #         for j in s2[i:i+s1_len]:
    #             check_alpha += alph[j]
    #         print(check_alpha, sum_alpha, s2[i:i+s1_len])
    #         if check_alpha == sum_alpha:
    #             return True

    #     return False


solution = Solution()

s1 = "ab"
s2 = "eidbaooo"
expected = True

print(solution.checkInclusion(s1, s2), '==', expected, ':', s1, s2)

s1 = "ab"
s2 = "eidboaoo"
expected = False
print(solution.checkInclusion(s1, s2), '==', expected, ':', s1, s2)

s1 = "ab"
s2 = "ba"
expected = True

print(solution.checkInclusion(s1, s2), '==', expected, ':', s1, s2)

s1 = "adc"
s2 = "dcda"
expected = True

print(solution.checkInclusion(s1, s2), '==', expected, ':', s1, s2)

s1 = "abc"
s2 = "ccccbbbbaaaa"
expected = False

print(solution.checkInclusion(s1, s2), '==', expected, ':', s1, s2)

s1 = "hello"
s2 = "ooolleoooleh"
expected = False

print(solution.checkInclusion(s1, s2), '==', expected, ':', s1, s2)

s1 = "qff"
s2 = "ifisnoskikfqzrmzlv"
expected = False

print(solution.checkInclusion(s1, s2), '==', expected, ':', s1, s2)
