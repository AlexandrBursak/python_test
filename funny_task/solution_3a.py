"""Queue To Do
===========
You're almost ready to make your move to destroy the LAMBCHOP doomsday device, but the security 
checkpoints that guard the underlying systems of the LAMBCHOP are going to be a problem. 
You were able to take one down without tripping any alarms, which is great! 
Except that as Commander Lambda's assistant, you've learned that the checkpoints are about to 
come under automated review, which means that your sabotage will be discovered and 
your cover blown -- unless you can trick the automated review system.

To trick the system, you'll need to write a program to return the same security checksum that 
the bunny trainers would have after they would have checked all the workers through. Fortunately, 
Commander Lambda's desire for efficiency won't allow for hours-long lines, so the trainers at 
the checkpoint have found ways to quicken the pass-through rate. Instead of checking each and 
every worker coming through, the bunny trainers instead go over everyone in line while noting 
their worker IDs, then allow the line to fill back up. Once they've done that they go over the 
line again, this time leaving off the last worker. They continue doing this, leaving off one more 
worker from the line each time but recording the worker IDs of those they do check, until they 
skip the entire line, at which point they XOR the IDs of all the workers they noted into 
a checksum and then take off for lunch. Fortunately, the workers' orderly nature causes them to 
always line up in numerical order without any gaps.

For example, if the first worker in line has ID 0 and the security checkpoint line holds three 
workers, the process would look like this:
0 1 2 /
3 4 / 5
6 / 7 8
where the trainers' XOR (^) checksum is 0^1^2^3^4^6 == 2.

Likewise, if the first worker has ID 17 and the checkpoint holds four workers, the process 
would look like:
17 18 19 20 /
21 22 23 / 24
25 26 / 27 28
29 / 30 31 32
which produces the checksum 17^18^19^20^21^22^23^25^26^29 == 14.

All worker IDs (including the first worker) are between 0 and 2000000000 inclusive, and 
the checkpoint line will always be at least 1 worker long.

With this information, write a function solution(start, length) that will cover for the missing 
security checkpoint by outputting the same checksum the trainers would normally submit before 
lunch. You have just enough time to find out the ID of the first worker to be checked (start) 
and the length of the line (length) before the automatic review occurs, so your program must 
generate the proper checksum with just those two values.

-- Python cases --
Input:
solution.solution(0, 3)
Output:
    2

Input:
solution.solution(17, 4)
Output:
    14
"""

import time
# from memory_profiler import profile

# @profile
def solution(start, length):
	line = 0
	for i in xrange(length):
		j_length = length - i
		for j in xrange(j_length):
			line ^= start
			start+=1
		start+=i

	return line

def solution_2(start, length):
	line = 0
	for i in range(length):
		move = 0
		if start%2:
			line^=start
			start+=1
			move=1

		i_length = length - i - move
		new_length = (i_length//4) * 4
		diff = i_length - new_length

		if diff > 0:
			curr_start = start + new_length
			curr_end = curr_start + diff
			line = reduce(lambda x, y: y^x, range(curr_start, curr_end), line)

		start += (length - move)

	return line



# def solution_2(start, length):
# 	def apply_formula(x, y):
# 		return y^x
# 	line = 0
# 	for i, begin in enumerate(xrange(start, start + length*length, length)):
# 		line = reduce(apply_formula, xrange(begin, begin + (length - i)), line)
# 	return line

# def solution_2(start, length):
# 	line = 0
# 	for i in xrange(length):
# 		j_length = start + (length - i)
# 		line = reduce(lambda x, y: y^x, xrange(start, j_length), line)
# 		start = i + j_length

# 	return line

# @profile
# def solution_2(start, length):
# 	ress = 0
# 	i = 0
# 	j = 0
# 	max_pos = length
# 	while True:
# 		if max_pos == i + j:
# 			i += j
# 			j += 1
# 			if j == length:
# 				break
# 			max_pos += length

# 		ress ^= (start + i)
# 		i += 1

# 	return ress

# @profile
# def solution_2(start, length):
# 	def get_lists(length):
# 		end = length**2
# 		col = 0
# 		row = 0
# 		while col < end:

# 			yield col

# 			if col + 1 + row == length * (row + 1):
# 				row += 1; col += row
# 			else:
# 				col += 1

# 	l = 0
# 	for k in get_lists(length):
# 		l ^= (start + k)
# 	return l

	# return reduce(lambda x, y: y^x, get_lists(start, length), 0)

# def solution_2(start, length):
# 	def get_lists(start, length):
# 		full_element = length*length - (length - 1)
# 		i = 0
# 		j = 0
# 		while i < full_element:

# 			yield (start + i)

# 			end_line = j * length + length

# 			if i + 1 >= end_line - j:
# 				i = end_line
# 				j += 1
# 				continue

# 			i += 1

# 	return reduce(lambda x, y: y^x, get_lists(start, length), 0)

# def solution_2(start, length):

# 	def apply_formula(x, y):
# 		return y^x

# 	ress = 0
# 	i = 0
# 	while i <= length:
# 		current_end = start + length - i
# 		ress = reduce(apply_formula, range(start, current_end), ress)
# 		start += length
# 		i += 1
# 	return ress	


print("=========Start=========")

start_time = time.time()
print(solution(0, 14))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2(0, 14))
print("--- %s seconds ---" % (time.time() - start_time))
print("=========0, 14=========")

start_time = time.time()
print(solution(3, 13))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2(3, 13))
print("--- %s seconds ---" % (time.time() - start_time))
print("=========3, 13=========")

start_time = time.time()
print(solution(2000000000, 1))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2(2000000000, 1))
print("--- %s seconds ---" % (time.time() - start_time))
print("=========2000000000, 1=========")

start_time = time.time()
print(solution(0, 1))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2(0, 1))
print("--- %s seconds ---" % (time.time() - start_time))
print("=========0, 1=========")

start_time = time.time()
print(solution(5, 1))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2(5, 1))
print("--- %s seconds ---" % (time.time() - start_time))
print("=========5, 1=========")

start_time = time.time()
print(solution(0, 3))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2(0, 3))
print("--- %s seconds ---" % (time.time() - start_time))
print("=========0, 3=========")

start_time = time.time()
print(solution(17, 4))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2(17, 4))
print("--- %s seconds ---" % (time.time() - start_time))
print("=========17, 4=========")

start_time = time.time()
print(solution(17, 100))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2(17, 100))
print("--- %s seconds ---" % (time.time() - start_time))
print("=========17, 100=========")

start_time = time.time()
print(solution(17, 5000))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2(17, 5000))
print("--- %s seconds ---" % (time.time() - start_time))
print("=========17, 5000=========")

start_time = time.time()
print(solution(15, 7689))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2(15, 7689))
print("--- %s seconds ---" % (time.time() - start_time))
print("=========15, 7689=========")

start_time = time.time()
print(solution(17, 15000))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2(17, 15000))
print("--- %s seconds ---" % (time.time() - start_time))
print("=========17, 15000=========")

