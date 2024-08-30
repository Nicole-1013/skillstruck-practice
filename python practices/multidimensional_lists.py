#cols = 3
#rows = 5
#list = []
#for x in range(rows):
    #list2 = []
    #for j in range(cols):
        #list2.append(5)
    #list.append(list2)

#print(list)
#----------------------------------------
#first_names = ["Nicole", "Lila", "Karla", "Omar"]
#last_names = ["Galvan", "Moreno", "Ayon", "Telix"]
#name_list = []
#for x in first_names:
    #names = []
    #for j in last_names:
        #names.append(x +" " + j)
    #name_list.append(names)
#print(name_list)
#---------------------------------------------
fruits = ["apple", "grape", "peach", "cinnamon", "vanilla"]
user_fruits = input("give me fruits").split()

combinations = [[x + " " + j for j in fruits] for x in user_fruits]
print(combinations)