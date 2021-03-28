import sys

def reversesort(L) :
    count = 0
    for i in range(len(L)-1) :
        j = L.index(min(L[i:]))
        L[i:j+1] = reversed(L[i:j+1])
        count += j - i + 1
    return count


T = int(sys.stdin.readline())

for i in range(1, T+1) :
    N = int(sys.stdin.readline())
    L = list(map(int, sys.stdin.readline().split()))
    result = reversesort(L)
    print("Case #{}: {}".format(i, result))
