table=int(input("Enter the number"))
for i in range(1,11):
    print(str(table)+"X" +str(i)+"="+str(i*table))
 #using f string table print
table=int(input("Enter the number"))
for i in range(1,11):
    print(f"{table}X{i}={table*i} ")