"""Control Flow :
1. Conditional Execution(if, else, elif loop)
2. Loops: Repeated Actions(for loop)
3. Loop based on condition(while loop)"""

""" Multiway Branching: elif """
y = 2
z = 1
for i in [1, 2, 3, 4, 5]:
    y = y * i
    z = z + 1
print(y)
print(z)

print("--"*189)

for i in range(1, 5):
    print(i)
print("--" *180)

""" using for loop"""
# program for find given no factors:
def factors(n):
    flist = []
    for i in range(1, n + 1):
        if (n % i) == 0:
            flist = flist + [i]
    return(flist)
print(factors(4))
print("--"*198)

""" Loop based on a condition:"""

def gcd(m, n):
    if  m < n:
        (m, n) = (n, m)
    while m % n != 0:
        (m, n) = (n, m % n)
    return(n)
print(gcd(12,4))
print(gcd(63,14))
print("--" *180)

def power(x, n):
    ans = 1
    for i in range(0, n):
        ans = ans * x
    return(ans)
print(power(3, 5))