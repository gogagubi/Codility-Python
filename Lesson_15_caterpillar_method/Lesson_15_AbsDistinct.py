def solution(A):
    N = len(A)
    left = 0
    right = N - 1
    ans = 0

    while left <= right:
        while left < right and A[left] == A[left + 1]:
            left += 1
        while left < right and A[right] == A[right - 1]:
            right -= 1

        le = abs(A[left])
        ri = abs(A[right])

        if le > ri:
            left += 1
            ans += 1
        elif ri > le:
            right -= 1
            ans += 1
        else:
            ans += 1
            left += 1
            right -= 1

    return ans


if True:
    A = [-5, -3, -1, 0, 3, 6]
    result = solution(A)
    print("Result ", result)

if True:
    A = [-5]
    result = solution(A)
    print("Result ", result)

if True:
    A = []
    result = solution(A)
    print("Result ", result)

if True:
    A = [1, 2, 3, 4]
    result = solution(A)
    print("Result ", result)

if True:
    A = [-2147483648, -1, 0, 1]
    result = solution(A)
    print("Result ", result)

if True:
    A = [-2147483648, -2147483648, 1, 1, 1]
    result = solution(A)
    print("Result ", result)
