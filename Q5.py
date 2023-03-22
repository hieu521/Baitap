lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
            ele = str(input())
            lst.append(ele) 
            lst.sort(key=lambda x:x.lower())
print(lst)