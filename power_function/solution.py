# pow(a, n) calculate a^n
def pow(a, n):
    if n == 0:
        return 1

    n_is_positive = True
    if n < 0:
        n_is_positive = False
        n *= -1

    result = 1

    while n:
        if n % 2 == 1:
            result *=  a
            n -= 1
        
        n //= 2
        a *= a

    return result if n_is_positive else 1/result

# recursive code
def pow_r(a, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / pow_r(a, -n)

    if n % 2 == 1:
        return a * pow_r(a, n-1)
    
    x = pow_r(a, n/2)
    return x * x

if __name__ == "__main__":
    print(pow(10, 3))
    print(pow_r(10, 3))

    print(pow(10, -3))
    print(pow_r(10, -3))

    print(pow(10, 4))
    print(pow_r(10, 4))

    print(pow(10, 0))
    print(pow_r(10, 0))

    print(pow(10, 1))
    print(pow_r(10, 1))

