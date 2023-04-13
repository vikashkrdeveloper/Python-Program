#Use the open function to read the  content of a file!
f = open('sample.txt','r')
data = f.read()
print(data)
f.close()