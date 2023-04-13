# creating an empty set
a=set()
print(type(a))
# Adding value of empty set
a.add(2)
a.add(5)
a.add(5)#Adding a value repeatedly does not changes a set
print(a)
#a.add({8:0})# throw an error cannot add list or dictionary to sets
print(a)
#length of the set
print(len(a))#print the lenght of this set
#Removal of an items
a.remove(5)#Removes 5 from set a
#a.remove(12)# throws an error  while  trying to remove 15(Which is not present in the set)
print(a)
#Removes an arlibrary element from the set and the element removed
print(a.pop)
print(a)
#creating Empties set 
print(a.clear)
print(a)
