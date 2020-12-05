def solution(S):
    stack = []

    for curr in S:
        if curr == ')':
            if len(stack) == 0:
                return 0

            stack.pop()
        else:
            stack.append(curr)

    if len(stack) == 0:
        return 1
    else:
        return 0


if True:
    S = '(()(())())'
    result = solution(S)
    print("Result ", result)

if True:
    S = '())'
    result = solution(S)
    print("Result ", result)
