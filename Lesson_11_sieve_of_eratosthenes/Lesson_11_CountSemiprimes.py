def sieve(N):
    primes = [True] * (N + 1)
    primes[0] = primes[1] = False

    i = 2
    while i * i <= N:
        j = i * i
        while j <= N:
            primes[j] = False
            j += i
        i += 1

    semiPrimes = [False] * (N + 1)
    i = 2
    while i * i <= N:
        if primes[i]:
            j = i * i
            while j <= N:
                if primes[j // i]:
                    semiPrimes[j] = True
                j += i

        i += 1

    return semiPrimes


def solution(N, P, Q):
    semiPrimes = sieve(N)

    dp = [0] * (N + 1)
    for i in range(1, len(dp)):
        dp[i] = dp[i - 1]
        if semiPrimes[i]:
            dp[i] += 1

    res = [0] * len(P)
    for i in range(0, len(P)):
        res[i] = dp[Q[i]] - dp[P[i] - 1]

    return res


if True:
    P = [1, 4, 16]
    Q = [26, 10, 20]
    N = 26

    result = solution(N, P, Q)
    print("Result ", result)
