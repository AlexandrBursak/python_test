class Solution:
    def reverse(self, x: int) -> int:
        
        int_32_poss = 2**31-1

        st = 1
        if x < 0:
            st = -1
            x *= st
        
        new_x = int(str(x)[::-1])
        
        if new_x > int_32_poss:
            return 0
        
        return new_x*st
    


solution = Solution()
print(solution.reverse(123), 321)
print(solution.reverse(1534236469), 0)
print(solution.reverse(1000000001), 1000000001)
print(solution.reverse(-2147483412), 2143847412)
