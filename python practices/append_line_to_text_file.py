#file = open("example.txt", "a")
#file.write("I love programming!")
#print(file.open())
#file.close()

#file = open("example.txt", "r")
#print(file.read())
#------------------------------------------
#file = open("letter.txt", "a")
#file.write("From your Pen Pal")
#___________________________________________

file = open("report.txt", "a")
file.write("Quote was said by Gandhi")
file.close()
file = open("example.txt", "r")
print(file.read())
file.close()