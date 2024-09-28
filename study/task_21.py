class Solution:
    def intToRoman(self, num: int) -> str:

        rome_dec = {
            0: ["I", "V"],
            1: ["X", "L"],
            2: ["C", "D"],
            3: ["M"],
        }

        i = 0
        list_num = ""
        while num:
            dec = num % 10
            if dec < 4:
                list_num = (rome_dec[i][0] * dec) + list_num
            elif dec <= 5:
                list_num = (rome_dec[i][0] * (5 - dec) + rome_dec[i][1]) + list_num
            elif dec < 9:
                list_num = (rome_dec[i][1] + rome_dec[i][0] * (dec - 5)) + list_num
            elif dec == 9:
                list_num = (rome_dec[i][0] + rome_dec[i + 1][0]) + list_num

            num = num // 10
            i += 1

        return list_num


solution = Solution()
print(solution.intToRoman(3749), 'MMMDCCXLIX')
print(solution.intToRoman(58), 'LVIII')
print(solution.intToRoman(1994), 'MCMXCIV')