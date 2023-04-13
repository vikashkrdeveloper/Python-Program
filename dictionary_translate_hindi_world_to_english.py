mydict={
    "pankha":"fan",
    "dabba":"box",
    "vastu":"item",
}
print("Option are ",mydict.keys())
a=input("Enter the hindi world\n")
# print("The meaning of your world is:",mydict[a])
# Bellow line will not throw an erro if the key is not present in the dictionary
print("The meaning of your world  is:",mydict.get(a))