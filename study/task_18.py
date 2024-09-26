class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
    
        mass = []
        while x != 0:
            mass.append(x%10)
            x = x//10

        for i in range(len(mass)//2):
            if mass[i] != mass[len(mass)-1-i]:
                return False
        return True

        
solution = Solution()
print(solution.isPalindrome(1), True)
print(solution.isPalindrome(121), True)
print(solution.isPalindrome(-121), False)