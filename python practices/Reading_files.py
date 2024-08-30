
file = open("example.txt", "r")
read = file.read()
print(len(read.split()))
file.close()