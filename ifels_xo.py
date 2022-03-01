def xo(size):
    left = 0
    right = size - 1
    for i in range(0, size):
        for j in range(0, size):
            if j == left or j == right:
                print("x", end = '')
            else:
                print("o", end = '')
        print()
        left = left + 1
        right = right -1
print(xo(5))