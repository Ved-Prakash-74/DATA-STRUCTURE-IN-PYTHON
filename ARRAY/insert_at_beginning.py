a=[]
n=int(input("How many elements you want to enter: "))
for i in range(0,n):
    ele=int(input("Enter element :"))
    a.append(ele)
print("Array element are:",a)
ele=int(input("Enter element which is to be inserted at beginning: "))
a.insert(0,ele)
print("After inserting array element are:",a)