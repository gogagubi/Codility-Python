def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


if True:
    result = gcd(18, 12)
    print("Result ", result)

if True:
    result = gcd(3, 10)
    print("Result ", result)
