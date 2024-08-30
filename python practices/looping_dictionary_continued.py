#ride = {
    #"Justin" : 65,
    #"Karla":66,
    #"Omar":70,
    #"Leslie": 102,
    #3"Simon":50
#}

#for x in ride.values():
    #if x >= 100:
        #print("This person is tall enough to ride.")
    #else:
        #print('This person is too short to ride')
#----------------------------------------------------------
#dictionary = { 
    #7: "first", 
    #3: "second", 
    #4: "third", 
    #8: "fourth", 
    #9: "fifth" 
#}
#my_list = [int(n) for n in input().split()]

#for x in my_list :
    #if x ==7:
        #print("Yes")
    #elif x == 3:
        #print("Yes")
    #elif x == 4:
        #print("Yes")
    #elif x == 8:
        #print("Yes")
    #elif x == 9:
        #print("Yes")
    #else:
        #print("No")
#----------------------------------------------------------
words = input("Give me a list of words").split()
mostFrequent = {}

for x in words:
    if x in mostFrequent:
        oldValue = mostFrequent.pop(x)
        mostFrequent[x] = oldValue + 1
    else:
        mostFrequent[x] = 1

maxVal = 0
for x,y in mostFrequent.items():
    if y > maxVal:
        maxVal = y
        maxKey = x

print(maxKey)

