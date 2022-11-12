#Mergesort Algoritması

"""
Write merge algorithm that merges 2 sorted arrays. Compute your algorithm running time as a function of n.

Example input=[1, 4, 5, 8], [2, 3, 6, 7] output=[1, 2, 3, 4, 5, 6, 7, 8]


Then integrate merge algorithm into mergesort algorithm shown in class. 
Run it on some example input, explain each step by using a debugger.
"""

arr1 = [1, 5, 4, 8]
arr2 = [2, 3, 6, 7, 9]
cnt = 1


def mergesort(arr):
    global cnt
    
    n=len(arr)
    if(n <= 1):
        return arr
    
    
    middle = n//2
     
    
    left = arr[:middle]
    mergesort(left)
    
    right = arr[middle:]
    mergesort(right) #hiçb
    
    leftCounter = 0
    rightCounter = 0
    arrayCounter = 0
    
    
    
    while leftCounter < len(left) and rightCounter < len(right):
        if left[leftCounter] <= right[rightCounter]:
            arr[arrayCounter] = left[leftCounter]
            leftCounter += 1
        else:
            arr[arrayCounter] = right[rightCounter]
            rightCounter += 1
        arrayCounter += 1
 
    while leftCounter < len(left):
        arr[arrayCounter] = left[leftCounter]
        leftCounter += 1
        arrayCounter += 1
 
    while rightCounter < len(right):
         arr[arrayCounter] = right[rightCounter]
         rightCounter += 1
         arrayCounter += 1
    
    
def main():
    arr = arr1 + arr2
    print(arr)
    print(mergesort(arr))
    print(arr,cnt)

main()





