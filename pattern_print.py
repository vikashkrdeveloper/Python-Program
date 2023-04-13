n=5

for i in range(5):
    print("*" *(i+1))
#print pattern
n=5
for i in range(5):
    print(" " * (n-i-1),end="")
    print("*" * (2*+i+1),end="")
    print(" " * (n-i-1))

