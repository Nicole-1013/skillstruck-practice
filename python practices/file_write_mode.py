#file = open("porcupine.txt", "w")
#file.write("In short, I love to code!")
#file.close()
#----------------------------------------------
#file = open("email.txt", "w")
#file.write("Never mind")
#file.close()
#-----------------------------------------------
answer = input("What do you want to say")
file = open("report.txt", "w")
file.write(answer)
file.close()
file = open("report.txt", "r")
print(file.read())
