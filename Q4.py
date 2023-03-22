lst = []
n = int (input(' Enter number of elements :'))

for i in range(0,n):
    ele = int(input('element '))
    lst.append(ele)

res = sorted(set(lst),key= lambda ele : lst.count(ele),reverse=True)
print(res)