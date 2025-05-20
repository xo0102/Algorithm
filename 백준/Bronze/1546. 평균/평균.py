num = int(input())

arr = list(map(int, input().split()))
maximum = max(arr)
sum=0

for i in range(num):
    arr[i]=arr[i]/maximum*100

for i in range(num):
    sum=sum+arr[i]

ave = sum/num
print(f"{ave:.2f}") 