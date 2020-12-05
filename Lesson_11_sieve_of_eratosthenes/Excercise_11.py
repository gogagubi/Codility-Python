# Get SEMI-PRIMARY numbers
def sieve(N):
    semi = set()
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False

    i = 2
    while i * i <= N:
        if sieve[i]:
            for j in range(i * i, N + 1, i):
                sieve[j] = False
        i += 1

    i = 2
    while i * i <= N:
        if sieve[i]:
            for j in range(i * i, N + 1, i):
                if j % i == 0 and sieve[j // i]:
                    semi.add(j)
        i += 1

    return semi


if True:
    N = 26
    result = sieve(N)
    print("Result ", result)
