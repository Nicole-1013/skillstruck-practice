#my_list = [[40, 45, 50], [6, 7, 8], [100, 200, 300], [50, 60, 70], [9, 0, 1]]

#rows = 5
#cols = 3

#for x in range(rows):
    #for j in range(cols):
        #my_list[x][j] = my_list[x][j] + 3
#print(my_list)
#---------------------------------------------------------------
my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]
user = int(input("give me num"))

rows = 4
cols = 3
for x in range(rows):
    for j in range(cols):
        my_list[x][j] *= user
print(my_list)
