import sys

def get_cost(X, Y, S) :
    result = 0

    S = S.replace("?", "")
    for i in range(len(S)-1):
        if S[i:i+2] == "CJ" :
            result += X
        elif S[i:i+2] == "JC" :
            result += Y

    return result

T = int(sys.stdin.readline())

for i in range(1, T+1) :
    line = sys.stdin.readline().split()
    X, Y, S = int(line[0]), int(line[1]), line[2].strip()
    result = get_cost(X, Y, S)
    print("Case #{}: {}".format(i, result))
