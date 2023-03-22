
a= [1,4,3,5,2]

f=[0]*len(a) # [0, 0, 0, 0, 0]
# print (f)
f[0]=1

for i in range(1,len(a)): #tao bien phu m  de set cac phan tu tim ra do dai don dieu dai nhat 
    m=0
    for j in range(i):
        if a[j]<a[i]:
            if f[j]>m:
                m=f[j]
            
        f[i]=m+1 # tinh ra duoc day day con day nhat la gi 

print(f)
