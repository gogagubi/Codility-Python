def check(A, k):
    n = len(A)
    boards = 0
    last = -1

    for i in range(0, n):
        if A[i] == 1 and last < i:
            boards += 1
            last = i + k - 1

    return boards


def boards(A, k):
    n = len(A)
    beg = 1
    end = n
    result = -1

    while beg <= end:
        mid = (beg + end) / 2
        if check(A, mid) <= k:
            end = mid - 1
            result = mid
        else:
            beg = mid + 1

    return result


if True:
    A = [0, 1, 0, 1, 1, 1, 0, 0, 1]
    k = 4
    result = boards(A, k)
    print("Result ", result)
