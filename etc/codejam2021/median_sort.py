# python interactive_runner.py python3 median_sort_test_tool.py 0 -- python3 median_sort.py

import sys

def ask(L) :
    print(" ".join(map(str, L)))
    res = int(input())
    L.remove(res)
    return res

def findSolution(target) :
    now = target[:3]
    mid = ask(now)
    small, big = [now[0]], [now[1]]

    for i in range(3, len(target)) :
        now = [small[0], mid, target[i]]
        response = ask(now)
        if response == mid :
            big.append(target[i])
        else :
            small.append(target[i])

    result = [mid]

    if len(small) == 1 :
        result = small + result
    elif len(small) == 2 :
        bs = ask([mid] + small)
        small.remove(bs)
        result = small + [bs] + result
    else :
        small = findSolution(small)
        bs = ask([small[0], small[-1], mid])
        if bs == small[0] :
            small = list(reversed(small))
        result = small + result
    
    if len(big) == 1 :
        result = result + big
    elif len(big) == 2 :
        sb = ask([mid] + big)
        big.remove(sb)
        result = result + [sb] + big
    else :
        big = findSolution(big)
        sb = ask([big[0], big[-1], mid])
        if sb == big[-1] :
            big = list(reversed(big))
        result = result + big

    return result


T, N, Q = map(int, input().split())

for i in range(1, T+1) :
    target = [ i for i in range(1, N+1) ]
    sol = findSolution(target)
    print(" ".join(map(str, sol)))
    res = int(input())
