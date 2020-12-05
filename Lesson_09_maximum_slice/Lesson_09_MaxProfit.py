def solution(A):
    profit = 0
    price = 200000

    for i in A:
        price = min(price, i)
        profit = max(profit, i - price)

    return profit


if True:
    A = [23171, 21011, 21123, 21366, 21013, 21367]
    result = solution(A)
    print("Result ", result)

if True:
    A = [4, 3, 6, 2]
    result = solution(A)
    print("Result ", result)

if True:
    A = [4, 3, 2, 3, 7, 6]
    result = solution(A)
    print("Result ", result)
