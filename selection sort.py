
def selectionsort(Values,n):
    for i in range(0,n):
        min=i
        for j in range(i+1,n):
            if Values[j]<Values[min]:
                min=j
        temp=Values[i]
        Values[i]=Values[min]
        Values[min]=temp
    return Values

n=int(input("Enter size -"))
Values=input("ENter Values").split()
Values=[int(v) for v in Values]
re=selectionsort(Values,n)
print(re)
