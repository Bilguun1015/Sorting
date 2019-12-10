# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i = 0
    while len(arrA) and len(arrB):
        if arrA[0] <= arrB[0]:
            merged_arr[i] = arrA[0]
            arrA = arrA[1:]
        else:
            merged_arr[i] = arrB[0]
            arrB = arrB[1:]
        i = i + 1
    
    while len(arrA):
        merged_arr[i] = arrA[0]
        arrA = arrA[1:]
        i = i + 1

    while len(arrB):
        merged_arr[i] = arrB[0]
        arrB = arrB[1:]
        i = i + 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr

    half_length_array = (len(arr) // 2)

    left = arr[0 :half_length_array]
    right = arr[half_length_array:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

print(merge_sort([6,5,4,2,1,7,5,1,0,0,2,3,4,5]))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
