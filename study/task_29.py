from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # if k ==0:
        #     return False

        # pos = 0
        # arr.sort()

        # res = True
        # while res:
        #     # print(arr[len(arr)-pos-1])
        #     # find = 10/arr[pos] 
        #     if (arr[pos] + arr[len(arr)-pos-1])%k:
        #         return False
        #     pos += 1
        #     if len(arr)//2 <= pos:
        #         break

        # return res

        count = [0] * k

        print(count)

        for i in arr:
            i %= k
            count[i] += 1
        
        print(count)

        if count[0] % 2 != 0:
            return False
        
        i = 1
        while i <= k / 2:
            print('count[i] != count[k-i]:', count[i], count[k-i])
            if count[i] != count[k-i]:
                return False
            i += 1
        

        return True


solution = Solution()

# arr = [-1,1,-2,2,-3,3,-4,4] 
# k = 3
# expected = True

# arr = [1,2,3,4,5,10,6,7,8,9]
# k = 5
# expected = True

arr = [1,2,3,4,5,6]
k = 10
expected = False

print(solution.canArrange(arr, k), expected)
