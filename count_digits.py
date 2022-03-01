def counts_digits(n):
     count = 0
     while n > 0 or n < 0:
         n = n // 10
         count += 1
     return count

print(counts_digits(12))
# def half_the_fun(number):
#     number = number // 2
#     for count in range(1, number + 1):
#         print(count, end=" ")
#     print()
# def main():
#     number = 8
#     half_the_fun(11)
#     half_the_fun(2 - 3 + 2 * 8)
#     half_the_fun(number)
#     print("number =", number)
# main()
#
# print(main())
#
#








