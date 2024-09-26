"""
Find the Access Codes
=====================
In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it. But the only door leading to the LAMBCHOP chamber is secured with a unique lock system whose number of passcodes changes daily. Commander Lambda gets a report every day that includes the locks' access codes, but only the Commander knows how to figure out which of several lists contains the access codes. You need to find a way to determine which list contains the access codes once you're ready to go in.

Fortunately, now that you're Commander Lambda's personal assistant, Lambda has confided to you that all the access codes are "lucky triples" in order to make it easier to find them in the lists. A "lucky triple" is a tuple (x, y, z) where x divides y and y divides z, such as (1, 2, 4). With that information, you can figure out which list contains the number of access codes that matches the number of locks on the door when you're ready to go in (for example, if there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).

Write a function solution(l) that takes a list of positive integers l and counts the number of "lucky triples" of (li, lj, lk) where the list indices meet the requirement i < j < k. The length of l is between 2 and 2000 inclusive. The elements of l are between 1 and 999999 inclusive. The solution fits within a signed 32-bit integer. Some of the lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0.

For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the solution 3 total.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========

-- Python cases --
Input:
solution.solution([1, 1, 1])
Output:
    1

Input:
solution.solution([1, 2, 3, 4, 5, 6])
Output:
    3
"""

import time
# from memory_profiler import profile

# def solution(l):
#     ress = list()
#     size = len(l)

#     for i, li in enumerate(l[0:size-2]):
#         for j, lj in enumerate(l[i+1:size-1]):
#             if lj%li == 0:
#                 for lk in l[i+1+j+1:size]:
#                     if lk%lj == 0:
#                         ress.append((li, lj, lk))
#     return len(ress)

# # @profile
# def solution(l):
#     ress = list()
#     size = len(l)

#     i = 0
#     while i < size-2:
#         li=l[i]
#         i+=1
#         for j, lj in filter(lambda x: x and x[1]%li==0, enumerate(l[i:size-1], i)):
#             ress.extend([
#                 (li, lj, lk) 
#                 for lk in l[j+1:size] if lk and lk%lj == 0
#             ])

#     return len(ress)

# def solution(l):
#     # ress = list()
#     ress = 0
#     size = len(l)
#     l_en = list(enumerate(l))

#     # import rpdb; rpdb.set_trace()

#     def filter_list(i, li):
#         # for index, el in enumerate(l[i:size-1], i):
#         for index, el in l_en[i:size-1]:
#             if el%li==0:
#                 yield index, el

#     i = 0
#     while i < size-2:
#         # li=l[i]
#         i+=1
#         for j, lj in filter_list(i, l[i]):

#             ress += len([lk for lk in l[j+1:size] if lk and lk%lj == 0])
#             # ress.extend([
#             #     (li, lj, lk) 
#             #     for lk in l[j+1:size] if lk and lk%lj == 0
#             # ])

#     # return len(ress)
#     return ress

def solution(l):
    ress = 0

    c = {}
    for i in range(0, len(l)):
        c[i] = 0
        for cj in range(0, i):
            if l[i]%l[cj]==0:
                c[i] = c[i] + 1
                ress = ress + c[cj]

    return ress

# def solution(l):
#     c = [0] * len(l)
#     print("[0] * len(l):", c)
#     count = 0

#     for i in range(0,len(l)):
#         j=0
#         for j in range(0, i):
#             if l[i] % l[j] == 0:
#                 c[i] = c[i] + 1
#                 count = count + c[j]
#     # print j

#     # print c
#     # print count
#     return count


# @profile
# def solution(l):
#     ress = 0
#     size = len(l)
#     # l_en = list(enumerate(l))

#     i = 0
#     while i < size-2:
#         i+=1
#         j=i
#         while j < size-1:
#             if l[j]%l[i] == 0:
#                 ress += len([lk for lk in l[j+1:size] if lk%l[j] == 0])
#             j+=1
#     return ress

# @profile
# def solution(l):
#     ress = 0
#     size = len(l)
#     l_en = list(enumerate(l))

#     i = 0
#     while i < size-2:
#         i+=1
#         for j, lj in l_en[i:size-1]:
#             if lj and lj%l[i] == 0:
#                 ress += len([lk for lk in l[j+1:size] if lk and lk%lj == 0])
#     return ress

# @profile
def solution_2(l):
    ress = 0
    size = len(l)

    i = 0
    while i < size-2:
        # li=l[i]
        i+=1
        for j, lj in enumerate(l[i:size-1], i):
            if lj and lj%l[i] == 0:
                # for lk in l[j+1:size]:
                #     if lk and lk%lj == 0:
                #         ress += 1
                # ress.extend([
                #     (li, lj, lk) 
                ress += len([lk for lk in l[j+1:size] if lk and lk%lj == 0])
                # ])

    # return len(ress)
    return ress

# def solution_2(l):
#     ress = list()
#     size = len(l)

#     for j, lj in enumerate(l[1:size-1]):
#         for i in l[0:j+1]:
#             if lj%i == 0:
#                 ress.extend([
#                     (i, lj, k) 
#                     for k in l[j+1+1:size] if k and k%lj == 0
#                 ])
#     return len(ress)

# def solution(l):
#     ress = list()
#     size = len(l)

#     if size < 2:
#         return 0

#     # print(l[:size-2])
#     # print(l[1:size-1])
#     # print(l[2:size])

#     ress=[
#         [l[:size-2]], 
#         [l[1:size-1]], 
#         [l[2:size]]
#     ]
#     # for i in 

#     # print(ress)

    

print("=========Start=========")

print("=========[1, 1, 1]=========")
start_time = time.time()
print(solution([1, 1, 1]))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2([1, 1, 1]))
print("--- %s seconds ---" % (time.time() - start_time))

print("=========[1, 1, 1, 2]=========")
start_time = time.time()
print(solution([1, 1, 1, 2]))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2([1, 1, 1, 2]))
print("--- %s seconds ---" % (time.time() - start_time))

print("=========[3, 4, 1]=========")
start_time = time.time()
print(solution([3, 4, 1]))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2([3, 4, 1]))
print("--- %s seconds ---" % (time.time() - start_time))

print("=========[1, 2, 3, 4, 5, 6]=========")
start_time = time.time()
print(solution([1, 2, 3, 4, 5, 6]))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2([1, 2, 3, 4, 5, 6]))
print("--- %s seconds ---" % (time.time() - start_time))

print("=========[1, 2, 3, 4, 5, 6, 7, 8]=========")
start_time = time.time()
print(solution([1, 2, 3, 4, 5, 6, 7, 8]))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2([1, 2, 3, 4, 5, 6, 7, 8]))
print("--- %s seconds ---" % (time.time() - start_time))

print("=========range(1, 51, 3)=========")
start_time = time.time()
print(solution(range(1, 51, 3)))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2(range(1, 51, 3)))
print("--- %s seconds ---" % (time.time() - start_time))

print("=========range(1, 999)=========")
start_time = time.time()
print(solution(range(1, 999)))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2(range(1, 999)))
print("--- %s seconds ---" % (time.time() - start_time))

print("=========range(1, 9999, 3)=========")
start_time = time.time()
print(solution(range(1, 9999, 7)))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2(range(1, 9999, 7)))
print("--- %s seconds ---" % (time.time() - start_time))

print("=========range(1, 99999, 5)=========")
start_time = time.time()
print(solution(range(1, 99999, 5)))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(solution_2(range(1, 99999, 5)))
print("--- %s seconds ---" % (time.time() - start_time))
