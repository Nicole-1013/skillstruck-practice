"""
stack = []
stack.append("a")
stack.append("b")
stack.append("c")
stack.append("d")
stack.pop()
print(stack)
"""
#---------------------------------------------------------------
"""
first = "r"
second = "t"
third = "s"
fourth = "y"
fifth = "o"
stack = []
stack.append(third)
stack.append(second)
stack.append(fifth)
stack.append(first)
stack.append(fourth)
print(stack)"""
#--------------------------------------------------------------
answer = ["apples", "steak", "potatoes", "carrots"]
user_input = input("add element")
if "s" in user_input.lower():
    answer.append(user_input)
    print(answer)
else:
    print("The input doesn't have the letter s")



