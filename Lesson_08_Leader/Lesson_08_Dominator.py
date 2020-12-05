def findLeader(A):
    meter = 1
    leader = A[0]

    for i in range(1, len(A)):
        if A[i] == leader:
            meter += 1
        else:
            meter -= 1

        if meter == 0:
            meter = 1
            leader = A[i]

    return leader


def solution(A):
    n = len(A)
    if n == 0:
        return -1

    half = n // 2
    leader = findLeader(A)
    occurrences = 0

    for k, v in enumerate(A):
        if v == leader:
            occurrences += 1
        if occurrences > half:
            return k

    return -1


if True:
    A = [3, 4, 3, 2, 3, -1, 3, 3]
    result = solution(A)
    print("Result ", result)
