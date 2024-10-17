import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))
        
        result_str = []

        while heap:
            count_n, char_n = heapq.heappop(heap)

            if len(result_str) >= 2 and result_str[-1] == result_str[-2] == char_n:
                if not heap:
                    break

                count_second, char_second = heapq.heappop(heap)

                # print('count_second, char_second', count_second, char_second)

                result_str.append(char_second)
                count_second += 1
                if count_second != 0:
                    heapq.heappush(heap, (count_second, char_second))

                heapq.heappush(heap, (count_n, char_n))
            else:
                # print('count_n, char_n', count_n, char_n)
                result_str.append(char_n)
                count_n += 1
                if count_n != 0:
                    heapq.heappush(heap, (count_n, char_n))
        
        return ''.join(result_str)


solution = Solution()

a = 1
b = 1
c = 7
expected = "ccaccbcc"

print(solution.longestDiverseString(a,b,c), '==', expected, ':', a,b,c)

a = 7
b = 1
c = 0
expected = "aabaa"

print(solution.longestDiverseString(a,b,c), '==', expected, ':', a,b,c)