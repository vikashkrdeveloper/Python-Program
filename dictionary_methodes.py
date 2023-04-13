mydic={
    "fast":"in a quecs manner",
    "vikash" : " a coder",
    "mark":"[2,6,9]",
   "vikashkumar":{'chapter1':'chapter2'},
   1:2
}
print(mydic.keys())
print(mydic.values())#print the values of the dictionary
print(mydic.items())#print the (key,values) of the dictionary
print(mydic)
updatedic={
    "vikash":"friend",
    "vishal":"friend",
    "vivek":"friend"

}
mydic.update(updatedic)#update the dictonary by adding key-values  pairs from updatedic
print(mydic)
print(mydic.get("vikash1"))#return none as vikash1 is not be present in the dictionary
# print(mydic("vikash1"))#throw an error as vikash1 is not be present in the dictionary