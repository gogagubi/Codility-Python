def solution(A, B):
    N = len(A)
    maxEl = max(A)

    fibonacci = [0] * (maxEl + 1)
    fibonacci[0] = fibonacci[1] = 1

    for i in range(2, len(fibonacci)):
        fibonacci[i] = (fibonacci[i - 2] + fibonacci[i - 1]) & ((1 << 30) - 1)

    result = [0] * N
    for i in range(0, N):
        result[i] = fibonacci[A[i]] & ((1 << B[i]) - 1)

    return result


if True:
    A = [4, 4, 5, 5, 1]
    B = [3, 2, 4, 3, 1]
    result = solution(A, B)
    print("Result ", result)
