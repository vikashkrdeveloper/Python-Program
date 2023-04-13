with open("anothe.txt","r") as f:
    a=f.read()
    print(a)
with open("anothe.txt","w") as f:
    a=f.write("me")
    print(a)
