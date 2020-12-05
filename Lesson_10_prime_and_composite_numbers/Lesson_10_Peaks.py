def solution(A):
    N = len(A)
    peakIndexes = []

    for i in range(1, N - 1):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            peakIndexes.append(i)

    candidates = len(peakIndexes)
    for candidate in range(candidates, 0, -1):
        if N % candidate == 0:
            found = [False] * candidate
            blockSize = N // candidate
            matched = 0

            for peakInd in peakIndexes:
                blockNumber = peakInd // blockSize
                if found[blockNumber] is not True:
                    found[blockNumber] = True
                    matched = matched + 1

                if matched == candidate:
                    return candidate

    return 0


if True:
    A = [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
    result = solution(A)
    print("Result ", result)
