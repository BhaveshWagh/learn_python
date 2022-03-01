def gcd(m, n):
    fm = []
    for i in range(1, m + 1):
        if (m % i) == 0:
            fm.append(i)

    fn = []
    for j in range(1, n + 1):
        if (n % j) == 0:
            fn.append(j)

    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)
    return (cf[-1])


print(gcd(14, 63))
print("_*_" * 180)


def gcd_1(m1, n1):  # Directly Compute
    cf = []
    for i in range(1, min(m1, n1) + 1):
        if (m1 % i) == 0 and (n1 % i) == 0:
            cf.append(i)
    return (cf[-1])


print(gcd_1(12, 14))
print("_*_" * 180)


def gcd_2(m2, n2):  # No list!
    for i in range(1, min(m2, n2) + 1):
        if (m2 % i) == 0 and (n2 % i) == 0:
            mrcf = i
    return (mrcf)


print(gcd_2(12, 14))
print(gcd_2(63, 14))
print("_*_" * 180)


def gcd_3(m3, n3):  # NO LIST!
    i = min(m3, n3)
    while i > 0:
        if (m3 % i) == 0 and (n3 % i) == 0:
            return (i)
        else:
            i = i - 1


print(gcd_3(12, 14))
print(gcd_3(63, 14))
print(gcd_3(48, 64))
print("_*_" * 180)


# Euclid's Algorithm :

def gcd_E(m4, n4):
    if m4 < n4:
        (m4, n4) = (n4, m4)
    if (m4 % n4) == 0:
        return n4
    else:
        diff = m4 - n4
    return gcd(max(n4, diff), min(n4, diff))


print(gcd_E(12, 14))
print(gcd_E(63, 14))
print(gcd_E(8, 4))
print("__" * 180)





def gcd1(a, b):
    if a < b:
        (a, b) = (b, a)
    while (a % b) != 0:
        diff1 = a - b
        (a, b) = (max(b, diff1), min(b, diff1))
    return b


print(gcd1(4, 20))
print(gcd1(14,63))
print("-+-"* 189)

def f(x):
    d=0
    y=1
    while y <= x:
        d=d+1
        y=y*3
    return(d)
print(f(846))
print("___*___" *220)

def h(n):
    s = 0
    for i in range(1,n+1):
        if n%i > 0:
           s = s+1
    return(s)
print(h(41))
print(h(40))
print("__ * __")

def g(m,n):
    res = 0
    while m >= n:
        res = res+1
        m = m-n
    return(res)
print(g(57,7))
print("+++++++++")