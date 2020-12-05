def solution(A, B, C):
    N = len(A)
    M = len(C)

    beg = 1
    end = M

    ans = -1
    while beg <= end:
        mid = beg + (end - beg) // 2
        prefixSum = [0] * (2 * M + 1)

        for i in range(0, mid):
            prefixSum[C[i]] += 1

        for i in range(1, 2 * M + 1):
            prefixSum[i] += prefixSum[i - 1]

        failed = False
        for i in range(0, N):
            if prefixSum[B[i]] == prefixSum[A[i] - 1]:
                failed = True
                break

        if failed:
            beg = mid + 1
        else:
            end = mid - 1
            ans = mid

    return ans


if True:
    A = [1, 4, 5, 8]
    B = [4, 5, 9, 10]
    C = [4, 6, 7, 10, 2]
    result = solution(A, B, C)
    print("Result ", result)

if True:
    A = [1, 6]
    B = [5, 7]
    C = [3, 2, 4, 6]
    result = solution(A, B, C)
    print("Result ", result)
