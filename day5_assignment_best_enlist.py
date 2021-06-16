#creating a list of n integers
n=int(input("Enter the no.of integers: "))
print("Enter the integers one by one:")
l=[]
for i in range(n):
    l.append(int(input()))
print("The list is: ",l)

#adding an item in to the list using function
l.append(3)
print("After adding 3 to the list by append(): ",l)

c=[10,11,12,13,14,15]
l.extend(c)
print("After adding a new list [10,11,12,13,14,15] by extend(): ",l)

l.insert(3,7)
print("After inserting 7 in index 3 by insert(): ",l)

#deleting item or items from the list
del l[5]
print("After deleting index 5 item by del: ",l)

del l[4:8]
print("After deleting index 4 to 7 items by del: ",l)

l.pop()
print("After removing last item by pop(): ",l)

l.pop(4)
print("After removing index 4 item by pop(): ",l)

l.remove(l[0])
print("After removing index 0 by remove(): ",l)

#storing largest number from the list to a variable
a=max(l)
print("Largest number in list: ",a)

#storing smallest number from the list to a variable
b=min(l)
print("Smallest number in list: ",b)

#creating a tuple and printing in reverse
tuple1=(1,2,3,4,5)
print("tuple1: ",tuple1)
print("After reversing tuple1",tuple1[::-1])

#creating a tuple and converting tuple into list
tuple2=("hi","hello","world")
print("tuple2: ",tuple2)
x=list(tuple2)
print("After converting tuple into list: ",x)
