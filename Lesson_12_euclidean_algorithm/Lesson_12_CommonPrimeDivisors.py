def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def hasCommonPrimeDivisor(a, b):
    while a > 1:
        div = gcd(a, b)
        if div == 1:
            break

        a /= div

    return a == 1


def solution(A, B):
    N = len(A)
    result = 0

    for i in range(0, N):
        if hasCommonPrimeDivisor(A[i], B[i]) and hasCommonPrimeDivisor(B[i], A[i]):
            result += 1

    return result


if True:
    A = [15, 10, 3]
    B = [75, 30, 5]

    result = solution(A, B)
    print("Result ", result)
