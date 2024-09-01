
import numpy as np
import random

lst = [[random.randint(0, 2) for i in range(16)] for i in range(1)]


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
    j = 0
    f = True
    newlst = []
    [first_length, max_length] = ags
    first = first_length if first_length > 0 else -first_length
    if max_length == first + 1:
        if lst[0] == 1:
            u = d = 0
        elif lst[0] == 0:
            u = 0
            d = first_length
        elif lst[0] == 2:
            d = 0
            u = first_length
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
    return newlst


def klist(lst, kils):
    if kils[-1] != 0:
        kils[-1] = 0
        for l in range(len(lst) - 1, -1, -1):
            if (lst[l] == 0 and kils[l] < kils[l - 1]) or (lst[l] == 1 and kils[l] == kils[l - 1]) or (lst[l] == 1 and kils[l] > kils[l - 1]):
                break
            elif lst[l] == 0:
                kils[l - 1] = kils[l] + 1
            elif lst[l] == 1:
                kils[l - 1] = kils[l]
            elif lst[l] == 2:
                kils[l - 1] = kils[l] - 1

    return kils



print(lst)

print("-"*100)

#print([[hlist(lst[i], longest(lst[i])) for i in range(len(lst))], [upon, down]])

#print([[hlist(lst[i], [max(longest(lst[i])[0], longest(lst[i][::-1])[0]), min(longest(lst[i])[1], longest(lst[i][::-1])[1])]) for i in range(len(lst))], [upon, down]])

#print([klist(lst[i], hlist(lst[i], [max(longest(lst[i])[0], longest(lst[i][::-1])[0]), min(longest(lst[i])[1], longest(lst[i][::-1])[1])])) for i in range(len(lst))])


List = [klist(lst[i], hlist(lst[i], [max(longest(lst[i])[0], longest(lst[i][::-1])[0]), min(longest(lst[i])[1], longest(lst[i][::-1])[1])])) for i in range(len(lst))]

print([List, [np.array(List).max(), np.array(List).min()]])
