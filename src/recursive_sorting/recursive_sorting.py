# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    return merged_arr

def divide(arr):
    #divide array into nested array of single-sorted elements
    # length = len(arr)
    if len(arr) > 1:
        half1 = arr[:len(arr)//2]
        half2 = arr[len(arr)//2:]
        arr.append(half1)
        arr.append(half2)
        arr = arr[:len(arr)//2]
        divide(arr)
    return arr
    # if length >1:
    #     half1 = arr[:length//2]
    #     half2 = arr[length//2:]
    #     nest.append(half1)
    #     nest.append(half2)
    #     divide(half1)
    #     divide(half2)
    # else:
    #     return nest


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    #divide first
    length = len(arr)
    if length >= 2:
        array

    return arr


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

if __name__ == '__main__':
    print(divide([1,2, 3, 4]))