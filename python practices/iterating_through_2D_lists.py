#my_list = [[40, 45, 50], [6, 7, 8], [100, 200, 300], [50, 60, 70], [9, 0, 1]]

#rows = 5
#cols = 3

#for x in range(rows):
    #for j in range(cols):
        #my_list[x][j] = my_list[x][j] + 3
#print(my_list)
#---------------------------------------------------------------
#my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]
#user = int(input("give me num"))

#rows = 4
#cols = 3
#for x in range(rows):
    #for j in range(cols):
        #my_list[x][j] *= user
#print(my_list)
#--------------------------------------------------------------
x = int(input("What is the first number?"))
y = int(input("What is the second number?"))
z = int(input("What is the third number?"))

my_list = [[0, 1, x], [10, 15, y], [100, 200, 300], [5, 6, z]]
max_num = my_list[0][0]

for x in range(4):
    for j in range(3):
        if my_list[x][j] > max_num:
            max_num = my_list[x][j]
print(max_num)
