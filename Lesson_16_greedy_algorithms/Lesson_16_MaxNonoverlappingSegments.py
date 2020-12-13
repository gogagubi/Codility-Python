def solution(A, B):
    N = len(A)
    if N == 0:
        return 0

    ans = 1
    end = B[0]
    for i in range(1, N):
        if A[i] > end:
            end = B[i]
            ans += 1

    return ans


if True:
    A = [1, 3, 7, 9, 9]
    B = [5, 6, 8, 9, 10]
    result = solution(A, B)
    print("Result ", result)

if True:
    A = [3, 7, 9, 1, 9]
    B = [6, 8, 9, 10, 10]
    result = solution(A, B)
    print("Result ", result)
