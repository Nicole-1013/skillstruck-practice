
arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
arr.append(int(input("Give me a number")))
def SelectionSort(arr):
    for i in range(len(arr)):
        smallest_number = i
        for j in range(i + 1, len(arr)):
            if arr[smallest_number] > arr[j]:
                smallest_number = j
        if arr[smallest_number] != i:
            new_num = arr[smallest_number]
            arr[smallest_number] = arr[i]
            arr[i] = new_num
    return arr
print(SelectionSort(arr))    