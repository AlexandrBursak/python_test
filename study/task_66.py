class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, unique_substrings):
            if start == len(s):
                return len(unique_substrings)

            max_splits = 0
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring not in unique_substrings:
                    unique_substrings.add(substring)
                    max_splits = max(max_splits, backtrack(end, unique_substrings))
                    unique_substrings.remove(substring)  # Backtrack step
            
            return max_splits

        return backtrack(0, set())

    # Fast but incorret solution
    # def maxUniqueSplit(self, s: str) -> int:
    #     len_s = len(s)
    #     if len_s == 1:
    #         return 1
        
    #     max_count = 0
        
    #     def set_current_max(new_s, start, end):
    #         nonlocal max_count
    #         sub_list = []
    #         sub_str = ''
    #         for char in new_s[start:start+len_s]:
    #             sub_str += char
    #             print(sub_str)
    #             if sub_str not in s:
    #                 sub_str = char
    #             if sub_str not in sub_list:
    #                 sub_list.append(sub_str)
    #                 sub_str = ''
                
    #         print(len(sub_list), sub_list)
    #         max_count = max(len(sub_list), max_count)
    #         if start >= len_s:
    #             return
    #         set_current_max(new_s, start+1, end+1)

    #     new_s = s + s
    #     set_current_max(new_s, 0, len_s)
    #     return max_count


solution = Solution()

expression = "ababccc"
expected = 5

print(solution.maxUniqueSplit(expression), '==', expected, ':', expression)
print('------')

expression = "wwwzfvedwfvhsww"
expected = 11

print(solution.maxUniqueSplit(expression), '==', expected, ':', expression)
print('------')

expression = "addbsd"
expected = 5

print(solution.maxUniqueSplit(expression), '==', expected, ':', expression)
print('------')

expression = "llkcegedae"
expected = 7

print(solution.maxUniqueSplit(expression), '==', expected, ':', expression)
print('------')

expression = "hbihebloyadb"
# # hb i h e b l o y a d
# "bihebloyadbh"
# # b i h e bl o y a s bh
# "ihebloyadbhb"
# # i h e b l o y a d hb
expected = 10

print(solution.maxUniqueSplit(expression), '==', expected, ':', expression)
print('------')

expression = "acefofckpkjfcdcp"
# # a c e f o fc k p kj fcd cp
# "cefofckpkjfcdcpa"
# # c e f o fc k p kj fcd cp a
# "efofckpkjfcdcpac"
# # e f o fc k p kj fcd c a 
# "fofckpkjfcdcpace"
# # f o fc k p kj fcd c a ce
expected = 12

print(solution.maxUniqueSplit(expression), '==', expected, ':', expression)
print('------')
