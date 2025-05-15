arr = [0,0,0,0,0,0,0,0,0]
for j in range(9):
   arr[j]=int(input())

max_value = 0
max_index = 0


for i in range(9):
    if arr[i]>max_value:
      max_value=arr[i]
      max_index=i+1


print(max_value)
print(max_index)