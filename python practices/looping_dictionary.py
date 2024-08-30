#measurement = {
    #'length' : 5,
    #'width' : 6,
    #'depth' : 10
#}
#for y in measurement.values():
   # print(y)
#-----------------------------------------------
#sum = 0
#group = { 
    #"Fred" : 12,
    #"Jackson" : 15,
   # "Sophie" : 20,
    #"Amanda" : 0, 
    #"Jane" : 0, 
#}
#firstInput = int(input("give me the first input"))
#secondInput = int(input("give me the second input"))

#group["Amanda"] = firstInput
#group["Jane"] = secondInput\

#for x in group.values():
    #sum += x

#print(sum)
#------------------------------------------------------

sum = 0
group = { 
    3 : 10, 
    5 : 3, 
    10 : 6, 
    4 : 30, 
}
firstKey = int(input("Give me a key"))
firstValue = int(input("Give me the value"))
group[firstKey] = firstValue

for x,y in group.items():
    product = x * y
    sum += product
print(sum)