num,x= map(int,input().split())

arr=list(map(int,input().split()))


for i in range(num):
    if arr[i] < x:
     print(arr[i])