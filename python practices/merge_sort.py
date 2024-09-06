arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
arr.append(int(input("give me a num")))
def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2
        l = arr[ :mid]
        r = arr[mid: ]
        mergeSort(l)
        mergeSort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j  += 1
            k += 1

        while i < len(l):
            arr[k] = l[i] 
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

mergeSort(arr)
print(arr)