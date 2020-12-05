import sys


def solution(N):
    i = 1
    perimeter = sys.maxsize

    while i * i <= N:
        if N % i == 0:
            perimeter = min(perimeter, (i + (N // i)) * 2)

        i = i + 1

    return perimeter


if True:
    N = 30
    result = solution(N)
    print("Result ", result)

if True:
    N = 9
    result = solution(N)
    print("Result ", result)
