import sys

def get_cost_list(N, C) :
    costs = [ 1 for x in range(N-1) ]
    rest = C - N + 1
    for i in range(N-1, 0, -1) :
        if rest == 0 :
            break
        elif rest >= i :
            costs[i-1] += i
            rest -= i
        else :
            costs[i-1] += rest
            break
    return costs

def reversesort_list(N, C) :
    if C < N - 1 or C > N * (N + 1) / 2 - 1 :
        return list()

    costs = get_cost_list(N, C)
    L = [ x for x in range(1, N+1) ]
    for c in costs :
        i = N - c
        L[i:] = reversed(L[i:])

    return L

    for i in range(len(L)-1) :
        j = L.index(min(L[i:]))
        L[i:j+1] = reversed(L[i:j+1])
        count += j - i + 1
    return count

def reversesort(L) :
    count = 0
    for i in range(len(L)-1) :
        j = L.index(min(L[i:]))
        L[i:j+1] = reversed(L[i:j+1])
        count += j - i + 1
    return count

T = int(sys.stdin.readline())

for i in range(1, T+1) :
    line = sys.stdin.readline().split()
    N, C = int(line[0]), int(line[1])
    result = reversesort_list(N, C)
    if not result : result = "IMPOSSIBLE"
    else : result = " ".join(map(str, result)) 
    print("Case #{}: {}".format(i, result))
