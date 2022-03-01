s = [1,2,3,4,5]
sum = 0
for i in range(0, len(s)):
    sum = sum + s[i]
print(sum)
# Write a function named has_midpoint that accepts three integers as parameters and returns
# if one of the integers is the midpoint between the other two integers;
# that is, if one integer is exactly halfway between them. Your function should return
# False if no such midpoint relationship exists. The integers could be passed in any order;
# the midpoint could be the 1st, 2nd, or 3rd. You must check all cases.
#
# Calls such as the following should return True:
#
# has_midpoint(4, 6, 8)
# has_midpoint(2, 10, 6)
# has_midpoint(8, 8, 8)
# has_midpoint(25, 10, -5)
# Calls such as the following should return False:
#
# has_midpoint(3, 1, 3)
# has_midpoint(1, 3, 1)
# has_midpoint(21, 9, 58)
# has_midpoint(8,2,  16)

# def has_midpoint(x,y,z):
#     if x < y < z:
#         return True
#     if x < y > z:
#         return True
#     if x == y == z:
#         return True
#     if x > y > z:
#         return True
#     else:
#         return False
# print(has_midpoint(4, 6, 8))
# print(has_midpoint(2, 10, 6))
# print(has_midpoint(8, 8, 8))
# print(has_midpoint(25, 10, -5))
#
# print(has_midpoint(3, 1, 3))
# print(has_midpoint(1, 3, 1))
# print(has_midpoint(21, 9, 58))
# print(has_midpoint(8,2,  16))
# # # # def contribution(count1, count2, sum, total):
# # #     sum = 1000
# # #
# # #     times = int(input("Is your money multiplied 1 or 2 times? "))
# # #
# # #     if times == 1:
# # #         donation = int(input("And how much are you contributing? "))
# # #         sum = sum + donation
# # #         count1 += 1
# # #         total += donation
# # #
# # #     if times == 2:
# # #         donation = int(input("And how much are you contributing? "))
# # #         sum = sum + 2 * donation
# # #         count2 += 1
# # #         total += donation
# #
# # def count_factors(n):
# #     count = 0
# #     for i in range(1, n + 1):
# #         if n % i == 0:   # a factor
# #            count = count + 1
# #     return count
# #
# # print(count_factors(12))
#
# # def zen(cents):
# #     return cents % 5 == 0
#
#
# # print(zen(45))
# # print(zen(455))
# # print(zen(5))
# # print(zen(44))