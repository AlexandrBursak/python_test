from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapper = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }
        
        letter = []
        for i in digits:
            num = int(i)

            symbols = mapper[num]

            if len(letter) == 0:
                letter = symbols
            else:
                trs_list = []
                for i in letter:
                    for j in symbols:
                        trs_list.append(i + j)
                letter = trs_list

        return letter


solution = Solution()

digits = "23"
expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]

print(solution.letterCombinations(digits), '==', expected, ':', digits)

digits = ""
expected = []

print(solution.letterCombinations(digits), '==', expected, ':', digits)

digits = "2"
expected = []

print(solution.letterCombinations(digits), '==', expected, ':', digits)

digits = "7"
expected = ['p', 'q', 'r', 's']

print(solution.letterCombinations(digits), '==', expected, ':', digits)
