def armstrong_numbers(n):
    for i in range(0, n + 1):
        sum = 0
    num = n
    while n > 0:
        digit = n % 10 
        sum = sum + pow (digit, 3)
        n = n // 10
    if sum == num:
        return True
    else:
        return False

print(armstrong_numbers(3));


