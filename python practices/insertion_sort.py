arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
user = int(input("Give me a number"))
arr.append(user)

def InsertionSort(arr):
    insert_spot = 0
    val_to_insert = 0
    for i in range(0, len(arr)):
        val_to_insert = arr[i]
        insert_spot = i
        while insert_spot > 0 and arr[insert_spot - 1] > val_to_insert:
            arr[insert_spot] = arr[insert_spot - 1]
            insert_spot = insert_spot - 1
        
        arr[insert_spot] = val_to_insert
    return arr


print(InsertionSort(arr))