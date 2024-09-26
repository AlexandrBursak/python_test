# coding: utf-8

import numpy as np

temperatures = np.random.randint(1,20,10)
k = len(temperatures)

print('Temperatures:', temperatures, k)
def temperature(t):
	
	i = 0
	while (i < k):
		current_day = t[i]
		j = i + 1
		while (j < k):
			next_day = t[j]
			if (current_day<next_day):
				print('+ For {} day with T:{} we should wait {} to next hotter day'.format(i+1, t[i], j-i))
				break
			j = j + 1
		else:
			print('- For {} day with T:{} we don\'t have the next hotter day'.format(i+1, t[i]))
		i = i + 1

	return k

temperature(temperatures)

print('========================== Stask =======================')


def temperature_2(t):

	i = k - 1
	stack = []
	while (i >= 0):
		if (len(stack)):


			if (stack[-1] > t[i]):
				stack.append(t[i])
			else:
				print('t[i]:', t[i])
				while (stack[-1] <= t[i]):
					stack.pop()
				stack.append(t[i])

			print('+ For {} day with T:{} we should wait {} to next hotter day'.format(i+1, t[i], len(stack)-1))


			print('All eleents:', stack)
			print('Last elements:', stack[-1])

		else:
			stack.append(t[i])
			print('- For {} day with T:{} we don\'t have the next hotter day'.format(i+1, t[i]))

		i = i - 1

temperature_2(temperatures)
