# Hey, I Already Did That!
# ========================
# Commander Lambda uses an automated algorithm to assign minions randomly to tasks, in order to keep minions on their toes. 
# But you've noticed a flaw in the algorithm -- it eventually loops back on itself, so that instead of assigning new minions 
# as it iterates, it gets stuck in a cycle of values so that the same minions end up doing the same tasks over and over again. 
# You think proving this to Commander Lambda will help you make a case for your next promotion.

# You have worked out that the algorithm has the following process:

# 1) Start with a random minion ID n, which is a nonnegative integer of length k in base b
# 2) Define x and y as integers of length k. x has the digits of n in descending order, and y has the digits of n in ascending order
# 3) Define z = x - y. Add leading zeros to z to maintain length k if necessary
# 4) Assign n = z to get the next minion ID, and go back to step 2

# For example, given minion ID n = 1211, k = 4, b = 10, then x = 2111, y = 1112 and z = 2111 - 1112 = 0999. 
# Then the next minion ID will be n = 0999 and the algorithm iterates again: x = 9990, y = 0999 and z = 9990 - 0999 = 8991, 
# and so on.

# Depending on the values of n, k (derived from n), and b, at some point the algorithm reaches a cycle, such as by reaching a constant value. 
# For example, starting with n = 210022, k = 6, b = 3, the algorithm will reach the cycle of values [210111, 122221, 102212] and 
# it will stay in this cycle no matter how many times it continues iterating. Starting with n = 1211, 
# the routine will reach the integer 6174, and since 7641 - 1467 is 6174, it will stay as that value no matter how many times it iterates.

# Given a minion ID as a string n representing a nonnegative integer of length k in base b, where 2 <= k <= 9 and 2 <= b <= 10, 
# write a function solution(n, b) which returns the length of the ending cycle of the algorithm above starting with n. 
# For instance, in the example above, solution(210022, 3) would return 3, since iterating on 102212 would return to 210111 
# when done in base 3. If the algorithm reaches a constant, such as 0, then the length is 1.


store = list()
def define_x_and_y(n):
	origin = [ch for ch in n]
	origin.sort(reverse=True)
	x = "".join(origin)
	origin.sort(reverse=False)
	y = "".join(origin)
	return x, y

BASE_STRING = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def to_base(number, base):
    result = ""
    while number:
        result += BASE_STRING[number % base]
        number //= base
    return result[::-1] or "0"

def define_diff_x_y(x, y, k, b):
	diff_x_y = int(x, b) - int(y, b)

	z = to_base(diff_x_y, b)

	if len(str(z)) < k:
		z = int(k - len(str(z))) * "0" + str(z)

	return z

def clear_store():
	store = list()

def store_or_break(z):
	if z not in store:
		store.append(z)
		return True
	else:
		return False

def solution(n, b):
	start_n = n
	k = len(n)
	if 2 > k or k > 9:
		return False
	if 2 > b or b >10:
		return False

	i = 1
	continue_cycle = True
	while continue_cycle:
		x, y = define_x_and_y(n)
		z = define_diff_x_y(x, y, k, b)
		n = z
		i+=1
		if store_or_break(z) == False:
			continue_cycle = False
			ress = len(store) - store.index(z)
		if int(n) == 0:
			continue_cycle = False
			ress = 1

	clear_store()
	return ress

# print(solution('1211', 10))
# print(solution('210022', 3))
# print(solution('1111', 10))
