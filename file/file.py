
A = input("Enter your name:")
file = open('file/text.txt','a+')
save_file = file.write("\n"+A)
file = open('file/text.txt','r')
print(file.read())
file.close()