def solution(N):
    count = 0
    i = 1
    while i * i <= N:
        if N % i == 0:
            if i * i == N:
                count = count + 1
            else:
                count = count + 2
        i = i + 1

    return count


if True:
    N = 24
    result = solution(N)
    print("Result ", result)

if True:
    N = 9
    result = solution(N)
    print("Result ", result)
