def findLeader(A):
    leader = A[0]
    meter = 1

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
    result = 0
    leader = findLeader(A)
    occurrences = 0

    for i in A:
        if i == leader:
            occurrences += 1

    leftLeaders = 0
    for k, v in enumerate(A):
        if v == leader:
            leftLeaders += 1

        rightLeaders = occurrences - leftLeaders
        if leftLeaders > (k + 1) / 2 and rightLeaders > (n - k - 1) / 2:
            result += 1

    return result


if True:
    A = [4, 3, 4, 4, 4, 2]
    result = solution(A)
    print("Result ", result)


if True:
    A = [4, 3, 4, 4, 4, 2, 4, 4, 4]
    result = solution(A)
    print("Result ", result)
