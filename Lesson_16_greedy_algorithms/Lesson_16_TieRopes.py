def solution(K, A):
    ans = 0
    curr = 0

    for i in A:
        curr += i
        if curr >= K:
            ans += 1
            curr = 0

    return ans


if True:
    K = 4
    A = [1, 2, 3, 4, 1, 1, 3]
    result = solution(K, A)
    print("Result ", result)  # expected 3

if True:
    K = 2
    A = [1, 2]
    result = solution(K, A)
    print("Result ", result)  # expected 1
