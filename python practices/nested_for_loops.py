#rows = 3
#pets = ["dog", "cat", "bird","hamster","pig"]
#my_list = [[j for j in pets] for x in range(rows)]
#print(my_list)
#-----------------------------------------------
#rows = int(input("how many rows do you want"))
#mylist = [1, 2, 3, 4, 5]
#list1 = [[j*rows for j in mylist] for x in range(rows)]
#print(list1)
#-----------------------------------------------
weather = input().split()
cols = ["windy", "breezy", "calm"]
weathers = [[x +" " + j for j in cols] for x in weather]
print(weathers)
