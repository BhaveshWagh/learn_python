def print_num_range(x, y):
    result =  []
    if x < y:
        for i in range(x, y + 1):
            result.append(i)
    else:
        if x > y:
            for j in range(x, y-1,-1):
                result.append(j)
        else:
            result.append(x)
    print(result)

print(print_num_range(1,5))
print(print_num_range(5,9))
print(print_num_range(8,1))

print("*"*90)
for i in range(8,1-1,-1):
    print(i)


