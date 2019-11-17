#this program is for append insert and extend function


l=eval(input("Enter elements in the list:"))
print("Entered list:",l)
l.append(input("Enter element to append"))
print("New list:",l)
l1=eval(input("Enter New list"))
l.extend(l1)
print("After adding new list in old one:",l)
