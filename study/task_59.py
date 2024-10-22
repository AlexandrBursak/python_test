class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        if n == 1 or k == 1:
            return '0'
    
        bit_lenght = (1 << n) - 1
        mid_of_bits_string = bit_lenght//2 + 1

        if mid_of_bits_string == k:
            return '1'
        elif mid_of_bits_string > k:
            return self.findKthBit(n-1, k)
        else:
            new_k = bit_lenght - k + 1
            return '1' if self.findKthBit(n-1, new_k) == '0' else '0'


solution = Solution()

n = 3
k = 1
expected = '0'

print(solution.findKthBit(n, k), '==', expected, ':', k, n)

n = 4
k = 11
expected = '1'

print(solution.findKthBit(n, k), '==', expected, ':', k, n)

n = 3
k = 5
expected = '0'

print(solution.findKthBit(n, k), '==', expected, ':', k, n)