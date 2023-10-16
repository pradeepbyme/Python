# comprehension : It is a process of creating new sequence
#                 using existing sequence.
# comprehensions can be applied on : List, Set, Dictionary, Generator.

# List Comprehension
# nums = [1, 577, 65, 78, 9237, 78, 45, 64, 32]
# even_nums = [num for num in nums if num % 2 == 0]
# print(even_nums)
# #
# # # Set Comprehension
# numset = {12,23,489,34,35,67}
# print(numset)
# numsetr = {numss+10 for numss in numset if numss % 2 == 0}
# print(numsetr)

# Nested List

# nums = [12, 24, 334, 5, 667, [34, 44, 45, 45], 56, 78]
# new_nums = [str(num) for num in nums]
# print(new_nums)                                         # Logic - less Python
# for i in new_nums[5]:
#     print(i)
# print(new_nums[5][1] + new_nums[5][2])

# Nested List Comprehension
new_list = [[j for j in range(0, 5)]for i in range(0, 9)]
for item in new_list:
    print(item)


#





