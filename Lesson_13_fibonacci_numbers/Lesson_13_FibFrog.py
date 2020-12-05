def fibonacci(N):
    arr = [1, 1]
    i = 2
    while arr[-1] < N:
        curr = arr[i - 1] + arr[i - 2]
        if curr > N:
            break

        arr.append(curr)
        i += 1

    return arr[1:]


def solution(A):
    A.append(1)
    N = len(A)
    dp = [-1] * N

    fib = fibonacci(N)
    fibSet = set(fib)

    for i in range(0, N):
        if A[i] == 1 and i + 1 in fibSet:
            dp[i] = 1
            continue

        if A[i] == 0:
            continue

        for f in fib:
            if i - f < 0:
                break

            if 0 < dp[i - f] and (dp[i] == -1 or dp[i - f] < dp[i]):
                dp[i] = dp[i - f] + 1

    return dp[N - 1]


if True:
    A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
    result = solution(A)
    print("Result ", result)

if True:
    A = [0, 1, 0, 1, 0, 1, 0, 1, 0]
    result = solution(A)
    print("Result ", result)
