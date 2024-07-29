
import random

upon, down = 0, 0

lst = [[random.randint(0, 2) for i in range(128)] for i in range(128)]

def longest(lst):
    turn = None
    first_length = 0
    max_length_two = 0
    max_length_zero = 0
    current_length_two = 0
    current_length_zero = 0

    for i in lst:
        if i == 0:
            current_length_zero += 1
            max_length_zero = max(max_length_zero, current_length_zero)
            current_length_two = 0
            if turn == None or turn == 0:
                first_length -= 1
                turn = 0
            else:
                turn = 1

        elif i == 2:
            current_length_two += 1
            max_length_two = max(max_length_two, current_length_two)
            current_length_zero = 0
            if turn == None or turn == 2:
                first_length += 1
                turn = 2
            else:
                turn = 1

        else:
            max_length_zero = max(max_length_zero, current_length_zero)
            max_length_two = max(max_length_two, current_length_two)

    return [first_length, max(max_length_zero, max_length_two) + 1]

def hlist(lst, ags):
    global upon, down
    j = 0
    f = True
    newlst = []
    [first_length, max_length] = ags
    first = first_length if first_length > 0 else -first_length
    for i in lst:
        if f == True:
            if i == 1:
                h = 0
            else:
                if i == 0:
                    h = -1
                elif i == 2:
                    h = 1
                first -= 1
                f = False
            newlst.append(h)
        elif first > 0:
            if i == 0:
                h -= 1
                first -= 1
            elif i == 2:
                h += 1
                first -= 1
            newlst.append(h)
        else:
            if f == False:
                if h == 0:
                    d = u = h
                if h < 0:
                    d = h
                    u = h + max_length - 1
                elif h > 0:
                    u = h
                    d = h - max_length + 1
                f = None
            if i == 1:
                j += 1
                newlst.append(h)
            elif i == 0:
                if mode == 2:
                    h = d
                    j = 1
                elif mode == 0:
                    h = d
                    j += 1
                    for k in range(1, j):
                        newlst[-k] += 1
                newlst.append(h)
            elif i == 2:
                if mode == 0:
                    h = u
                    j = 1
                elif mode == 2:
                    h = u
                    j += 1
                    for k in range(1, j):
                        newlst[-k] -= 1
                newlst.append(h)
        if i != 1:
            mode = i
    if u > upon:
        upon = u
    if d < down:
        down = d
    return newlst

print(lst)

print([[hlist(lst[i], longest(lst[i])) for i in range(len(lst))], [upon, down]])
