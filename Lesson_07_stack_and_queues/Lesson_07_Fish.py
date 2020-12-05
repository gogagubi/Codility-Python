def solution(A, B):
    n = len(A)
    eaten = 0
    stack = []

    for k, v in enumerate(A):
        if B[k] == 1:
            stack.append(v)
        else:
            while len(stack) > 0:
                eaten += 1
                if stack[-1] > v:
                    break
                else:
                    stack.pop()

    return n - eaten


if True:
    A = [4, 3, 2, 1, 5]
    B = [0, 1, 0, 0, 0]
    result = solution(A, B)
    print("Result ", result)

if True:
    A = [3, 4, 1, 2, 5, 6]
    B = [0, 1, 0, 0, 0, 1]
    result = solution(A, B)
    print("Result ", result)

if True:
    A = [3, 4, 1, 2, 5, 6]
    B = [0, 1, 0, 1, 0, 1]
    result = solution(A, B)
    print("Result ", result)
