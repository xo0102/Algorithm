num = int(input())

arr = list(map(int,input().split()))


min=arr[0]
max=arr[0]
for i in range(1,num):
    if arr[i]>max:
        max=arr[i]
    if arr[i]<min:
        min=arr[i]


print(min, max)