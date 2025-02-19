def karatsuba(x: int, y: int) -> int:
 if x < 10 or y < 10:
     return x * y
 else:
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    a = x // (10 ** (half)) # A = parte a esquerda de x
    b= x % (10 ** (half)) # B = parte a direita de x
    c = y // (10 ** (half)) # C = parte a esquerda de y
    d = y % (10 ** (half)) # D = parte a direita de y
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
    return ac * (10 ** (2 * half)) + (ad_plus_bc * (10 ** half)) + bd   