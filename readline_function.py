#Use the open function to readline the  content of a file!
f = open('sample.txt','r')
data = f.readline()
print(data)
data = f.readline()
print(data)
data = f.readline()
print(data)
f.close()