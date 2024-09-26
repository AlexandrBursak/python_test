def solution(x, y):
    
    if len(set(x)) > len(set(y)):
        new_list = set(x) - set(y)
    else:
        new_list = set(y) - set(x)


    return str(list(new_list)[0])


print(solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]))

print(solution([13, 5, 6, 2, 5], [5, 2, 5, 13]))
