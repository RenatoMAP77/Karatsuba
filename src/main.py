def karatsuba(x: int, y: int) -> int:
 if x < 10 or y < 10:
     return x * y
 else:
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    a = x // (10 ** (half)) #Left part of x
    b= x % (10 ** (half)) # Right part of x
    c = y // (10 ** (half)) # Left part of y
    d = y % (10 ** (half)) # Right part of y
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
    return ac * (10 ** (2 * half)) + (ad_plus_bc * (10 ** half)) + bd

 