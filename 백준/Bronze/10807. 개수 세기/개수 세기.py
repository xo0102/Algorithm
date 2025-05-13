num= int(input())

arr=list(map(int,input().split()))

x= int(input())
a=0

for i in range(num):
    if arr[i]==x:
        a+=1

print(a)