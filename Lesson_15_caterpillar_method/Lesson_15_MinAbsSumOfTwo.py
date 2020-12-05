def solution(A):
    N = len(A)
    ans = 2000000000
    P = 0
    Q = N - 1
    A.sort()

    while P <= Q:
        ans = min(ans, abs(A[P] + A[Q]))
        if abs(A[P]) > abs(A[Q]):
            P += 1
        else:
            Q -= 1

    return ans


if True:
    A = [1, 4, -3]
    result = solution(A)
    print("Result ", result)

if True:
    A = [-8, 4, 5, -10, 3]
    result = solution(A)
    print("Result ", result)
