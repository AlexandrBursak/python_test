def exec_smth(a, b):
	if a == b:
		return "="
	if a < b:
		main, second, lt, rt = b, a, "<", ">"
	if a > b:
		main, second, lt, rt = a, b, ">", "<"

	s1 = main**second
	s2 = second
	i = 1
	while i < main:
		s2*=second
		if s2 > s1:
			break
		i += 1

	if s1 > s2:
		return lt
	elif s1 < s2:
		return rt
	return "="

def get_equation(a, b):
	"""
    Test A**B <> B**A

    >>> get_equation(2, 3)
    '<'
    >>> get_equation(2, 4)
    '='
    >>> get_equation(3, 2)
    '>'
    >>> get_equation(2, 5)
    '>'
    >>> get_equation(1000, 999)
    '<'
    >>> get_equation(50, 999)
    '>'
    """

	if a == b:
		return "="
	elif a > 4 or b > 4:
		if a < b:
			return ">"
		return "<"
	else:
		s1 = a**b
		s2 = b**a
		if s1 > s2:
			return ">"
		elif s1 < s2:
			return "<"
		return "="



num1 = int(input()) 
num2 = int(input())

result = exec_smth(num1, num2)
print(result)
result = get_equation(num1, num2)
print(result)
