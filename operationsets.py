#Write a program to create a set and perform the following operations on that set- 1. Create a set with integer elements 2. Create a set with mixed data type elements 3. Create another set with elements - 1, 2, 3, 4, 3, 2 4. Create a set from a list with elements - [1, 2, 3, 2] 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]

set1 = {1,2,3,5} 
print(set1)
set2 = {1,"e",1.22,True}
print(set2)
set3 = {1,2,3,2,1,43,32,32,43}
print(set3)
set4 = set([12,33,44,55,55])
print(set4)
set4.pop()
print(set4)