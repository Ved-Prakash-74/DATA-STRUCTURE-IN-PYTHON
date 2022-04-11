a=[]
n=int(input("How many elements you want to enter: "))
for i in range(0,n):
    ele=int(input("Enter element :"))
    a.append(ele)
print("Array element are:",a)
pos=int(input("Enter position where you want to insert element: "))
ele=int(input("Enter element which is to be inserted in the given position: "))
a.insert(pos-1,ele)
print("After inserting array element are:",a)