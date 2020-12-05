def solution(A):
    N = len(A)
    K1 = [0] * N
    K2 = [0] * N

    for i in range(1, N - 1):
        K1[i] = max(K1[i - 1] + A[i], 0)

    for i in range(N - 2, 0, -1):
        K2[i] = max(K2[i + 1] + A[i], 0)

    maxSum = 0
    for i in range(1, N - 1):
        maxSum = max(K1[i - 1] + K2[i + 1], maxSum)

    return maxSum


if True:
    A = [3, 2, 6, -1, 4, 5, -1, 2]
    result = solution(A)
    print("Result ", result)

if True:
    A = [0, 10, -5, -2, 0]
    result = solution(A)
    print("Result ", result)
