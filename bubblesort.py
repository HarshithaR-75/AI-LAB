def bubblesort(arr):
    n=len(arr)
    for i in range (n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

n=int(input("Enter the size of the array"))
arr=[]
print("Enter the elements of the array")
for i in range (0,n):
    ele=int(input())
    arr.append(ele)
print("Original array")
print(arr)
bubblesort(arr)
print("Sorted array")
print (arr)
  