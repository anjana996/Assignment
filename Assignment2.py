lst = []
limit= int(input("Enter number of elements : "))

for i in range(0, limit):
    ele = int(input())

    lst.append(ele)

print("The input list :",lst)
new=[]
sum=0
for num in lst:
    if num>5:
        sum=num+1
        new.append(sum)

    elif num==5:
        new.append(num)
    else:
        sum=num-1
        new.append(sum)
print("The new list:",new)
