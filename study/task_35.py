from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total_sum = sum(skill)
        number_group = len(skill) / 2

        if total_sum % number_group:
            return -1
        
        skill_for_group = total_sum / number_group

        skill.sort()

        group_skills = 0
        for i in range(int(number_group)):
            first_player = skill[i]
            second_player = skill[len(skill)-1-i]

            if first_player + second_player != skill_for_group:
                return -1
            
            group_skills += first_player * second_player

        return group_skills


solution = Solution()

skill = [3,2,5,1,3,4]
expected = 22

print(solution.dividePlayers(skill), '==', expected, ':', skill)

skill = [2,3,4,2,5,5]
expected = 32

print(solution.dividePlayers(skill), '==', expected, ':', skill)
