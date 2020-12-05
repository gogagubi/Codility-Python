def solution(A):
    N = len(A)
    A.sort()
    ans = 0

    for P in range(0, N - 2):
        Q = P + 1
        R = P + 2
        while R < N:
            if A[P] + A[Q] > A[R]:
                ans += R - Q
                R += 1
            elif Q < R - 1:
                Q += 1
            else:
                Q += 1
                R += 1

    return ans


if True:
    A = [10, 2, 5, 1, 8, 12]
    result = solution(A)
    print("Result ", result)

if True:
    A = [3, 3, 5, 6]
    result = solution(A)
    print("Result ", result)

if True:
    A = [3, 3, 4, 5, 7]
    result = solution(A)
    print("Result ", result)
