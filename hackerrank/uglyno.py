def ugly(n):
    a = 2
    if n > 1:
        while a <= 5:
            if n % a == 0:
                n //= a
            else:
                a += 1
        return n == 1
    return False


print(ugly(27))
