a=[]
n=int(input("How many elements you want to enter: "))
for i in range(0,n):
    ele=int(input("Enter element :"))
    a.append(ele)
print("Array element are:",a)
ele=int(input("Enter element which is to be inserted at end: "))
a.append(ele)
print("after inserting array element are:",a)