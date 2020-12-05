def solution(A):
    maxElement = max(A)

    divisors = {}
    counts = {}
    for i in A:
        divisors[i] = set([1, i])
        counts[i] = counts[i] + 1 if i in counts else 1

    i = 2
    while i * i <= maxElement:
        j = i
        while j <= maxElement:
            if j in divisors and i not in divisors[j]:
                divisors[j].add(i)
                divisors[j].add(j // i)
            j += i
        i += 1

    result = [0] * len(A)
    for k, j in enumerate(A):
        result[k] = (len(A) - sum(counts.get(divisor, 0) for divisor in divisors[j]))

    return result


if True:
    A = [3, 1, 2, 3, 6]
    result = solution(A)
    print("Result ", result)

if True:
    A = [3, 2, 3, 6]
    result = solution(A)
    print("Result ", result)
