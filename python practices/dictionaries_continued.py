#coins = {
    #'pennies' : 10,
    #'nickels' : 15,
    #'dimes' : 12,
    #'quarters' : 3
#}
#coins['silver_dollar'] = 10
#coins.pop('pennies')
#print(coins)
#print(len(coins))


#dictionary = { 
    #1: "bicycle",
   # 2: "soccer balls",
   # 3: "piano books",  
#}
#fourth_item = input("give me sum")
#fifth_item = input("give me sum")
#sixth_item = input("give me sum")
#dictionary[4] = fourth_item
#dictionary[5] = fifth_item
#dictionary[6] = sixth_item
#print(dictionary)

work = {
    "Monday": 8,
    "Tuesday":9,
    "Wednesday":7,
    "Thursday":6,
    "Friday": 2
}
work["Saturday"] = 6
work.pop("Wednesday")
print(len(work))

if "Friday" in work:
    print("I worked Friday")
