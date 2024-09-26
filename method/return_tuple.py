need = True

def something_med(value):
	if value:
		return 1, 2
	return None, None


val, res = something_med(need)
print(val)

if val:
	print('Doing something')

