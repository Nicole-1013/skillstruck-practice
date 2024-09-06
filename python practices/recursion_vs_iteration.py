
'''def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * (factorial(num - 1))

print(factorial(int(input("Give me a number"))))'''
#---------------------------------------------------
'''def addNums(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + addNums(nums[1: ])

list_of_nums = [int(n) for n in input().split()]
print(addNums(list_of_nums))'''
#-----------------------------------------------------
nums_list = []
num = int(input("Give me a num"))


def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

for i in range(0, num):
    nums_list.append(fibonacci(i))
print(nums_list)
