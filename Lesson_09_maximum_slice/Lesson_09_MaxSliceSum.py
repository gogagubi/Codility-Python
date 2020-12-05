def solution(A):
    dp = A[0]
    sum = A[0]

    for i in range(1, len(A)):
        dp = max(dp + A[i], A[i])
        sum = max(sum, dp)

    return sum


if True:
    A = [3, 2, -6, 4, 0]
    result = solution(A)
    print("Result ", result)


if True:
    A = [-1, 0, -2, -7]
    result = solution(A)
    print("Result ", result)

if True:
    A = [-1, -8, -2, -7]
    result = solution(A)
    print("Result ", result)
