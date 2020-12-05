def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def solution(N, M):
    return N // gcd(N, M)


if True:
    N = 10
    M = 4

    result = solution(N, M)
    print("Result ", result)

if True:
    N = 12
    M = 4

    result = solution(N, M)
    print("Result ", result)
