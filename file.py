myfile = open('index.txt', 'r')
print(myfile.read())
print(myfile.write('Super puper'))
print(myfile.read())
myfile.close()