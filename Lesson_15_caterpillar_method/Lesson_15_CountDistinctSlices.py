def solution(M, A):
    N = len(A)
    ans = 0
    P = 0
    Q = 0
    seen = [False] * (M + 1)
    limit = 1000000000

    while Q < N:
        if seen[A[Q]] is not True:
            ans += (Q - P + 1)
            if ans >= limit:
                return limit

            seen[A[Q]] = True
            Q += 1
        else:
            seen[A[P]] = False
            P += 1

    return ans


if True:
    A = [3, 4, 5, 5, 2]
    M = 6
    result = solution(M, A)
    print("Result ", result)

if True:
    A = [5, 3, 4, 5, 2, 1]
    M = 6
    result = solution(M, A)
    print("Result ", result)
