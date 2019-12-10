# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for num in range(cur_index, len(arr)):
            if arr[num] < arr[smallest_index]:
                smallest_index = num

        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr
print(selection_sort([9,3,5,4,7,5,1]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    isSorted = False
    for i in range(0, len(arr)):
        cur_index = i
        for num in range(0,  cur_index):
            if arr[num] > arr[num+1]:
                isSorted = True
                arr[num+1], arr[num] = arr[num], arr[num + 1]
                if isSorted :
                    bubble_sort(arr)
    return arr

print(bubble_sort([9,3,5,4,7,5,1]))
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr