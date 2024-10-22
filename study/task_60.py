from typing import List, Union

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        def convert_to_bool(convert_value):
            return convert_value == 't'

        if len(expression) == 1:
            return convert_to_bool(expression)

        def getSubstr(condition: str, expression: str) -> List:
            current_condition = ''
            res = None

            i = 0
            while i < len(expression):
                count_i = 1

                current_element = expression[i]

                if current_element in ['&', '|', '!']:
                    current_condition = current_element
                    current_element, count_i = getSubstr(current_condition, expression[i+2:])

                elif current_element == ')':
                    # line = 't,f,t,f'
                    if condition == '!':
                        return not res, i + 3
                    
                    else:
                        return res, i + 3
                elif expression[i] == ',':
                    i += 1
                    continue

                if current_element in ['t', 'f']:
                    current_element = convert_to_bool(current_element)

                if res is not None:
                    if condition == '|':
                        res |= current_element
                    else:
                        res &= current_element
                else:
                    res = current_element
                i += count_i

            return res, i

        res, _ = getSubstr('', expression)
        return res


solution = Solution()

# expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.

expression = "&(t,t,t)"
expected = True

print(solution.parseBoolExpr(expression), '==', expected, ':', expression)
print('------')

expression = "&(|(f))"
expected = False

print(solution.parseBoolExpr(expression), '==', expected, ':', expression)
print('------')

expression = "&(|(f,f,f,t),|(f,t,f))"
expected = True

print(solution.parseBoolExpr(expression), '==', expected, ':', expression)
print('------')

expression = "!(&(f,t))"
expected = True

print(solution.parseBoolExpr(expression), '==', expected, ':', expression)
print('------')

