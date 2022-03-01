print('....1')
print('...2.')
print('..3..')
print('.4...')
print('5....')
print("--" * 90)
dot = 4
for i in range (1, 6):
    print("." * dot , i ,"." * (i - 1),sep='')
    dot -= 1


print("\\" *90)
def print_pattern(num):
    for i in range(1, num + 1):
        print("." * (num - i) + "*" * i)

print(print_pattern(5))