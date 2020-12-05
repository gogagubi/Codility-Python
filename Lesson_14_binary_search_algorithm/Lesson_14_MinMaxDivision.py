def isBlockValid(A, maxCount, maxSum):
    currSum = 0
    currCount = 0

    for i in A:
        currSum += i

        if currSum > maxSum:
            currSum = i
            currCount += 1

        if currCount >= maxCount:
            return False

    return True


def solution(K, M, A):
    lower = max(A)
    upper = sum(A)

    if K == 1:
        return upper

    if K >= len(A):
        return lower

    while lower < upper:
        mid = lower + (upper - lower) // 2
        if isBlockValid(A, K, mid):
            upper = mid
        else:
            lower = mid + 1

    return lower


if True:
    K = 3
    M = 5
    A = [2, 1, 5, 1, 2, 2, 2]
    result = solution(K, M, A)
    print("Result ", result)
