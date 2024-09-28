class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        number = 0

        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i + 1]]:
                number -= m[s[i]]
            else:
                number += m[s[i]]
        
        return number

    # def romanToInt(self, s: str) -> int:

    #     rome_number = {
    #         3000: 'MMM',
    #         2000: 'MM',
    #         1000: 'M',
    #         900: 'CM',
    #         800: 'DCCC',
    #         700: 'DCC',
    #         600: 'DC',
    #         500: 'D',
    #         400: 'CD',
    #         300: 'CCC',
    #         200: 'CC',
    #         100: 'C',
    #         90: 'XC',
    #         80: 'LXXX',
    #         70: 'LXX',
    #         60: 'LX',
    #         50: 'L',
    #         40: 'XL',
    #         30: 'XXX',
    #         20: 'XX',
    #         10: 'X',
    #         9: 'IX',
    #         8: 'VIII',
    #         7: 'VII',
    #         6: 'VI',
    #         5: 'V',
    #         4: 'IV',
    #         3: 'III',
    #         2: 'II',
    #         1: 'I',
    #     }
    #     number = 0
    #     for i in rome_number:
    #         try:
    #             if s.index(rome_number[i]) == 0:
    #                 s = s.replace(rome_number[i], '', 1)
    #                 number += i
    #         except:
    #             pass

    #     return number


solution = Solution()
print(solution.romanToInt('III'), 3)
print(solution.romanToInt('MMMDCCXLIX'), 3749)
print(solution.romanToInt('LVIII'), 58)
print(solution.romanToInt('MCMXCIV'), 1994)