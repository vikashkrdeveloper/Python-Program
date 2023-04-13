#print continue statement
for i in range(80):
    print(i)
    if i==3:
     print("continue statement is done")
    continue
#print continue statement skiping continue
for i in range(10):
    if i==3:
     print("continue statement is done")
     continue
    print(i)