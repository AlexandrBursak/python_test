# coding: utf-8
from numpy import random
import numpy as np

numbers = np.random.randint(-10,10,10)
numbers.sort()
numbers = np.unique(numbers)
k = random.randint(5)

print('k', k)
print('numbers', numbers)

def twoSum(numbers, k):
	i = 0
	j = len(numbers)-1
	while (i<j):
		sum = numbers[i]+numbers[j]

		print('- sum', sum, numbers[i], numbers[j])
		if sum > k:
			j=j-1
		elif sum < k:
			i=i+1
		else:
			return [numbers[i], numbers[j]]
	return []

print (twoSum(numbers, k))