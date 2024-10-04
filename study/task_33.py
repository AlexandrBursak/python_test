from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        str_dict = {}
        for item in f"{s1} {s2}".split(" "):
            # str_dict[item] = str_dict.get(item, 0) + 1
            if item not in str_dict:
                str_dict[item] = 0
            str_dict[item] += 1
        
        return [key for key in str_dict.keys() if str_dict[key] == 1]


solution = Solution()

s1 = "this apple is sweet"
s2 = "this apple is sour"
expected = ["sweet","sour"]

print(solution.uncommonFromSentences(s1, s2), '==', expected, ':', s1, s2)
