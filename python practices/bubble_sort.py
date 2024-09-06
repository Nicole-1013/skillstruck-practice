
'''arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
arr.append(int(input("Give me a num")))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                new_number = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = new_number
    return(arr)
print(bubble_sort(arr))'''
#---------------------------------------------------

