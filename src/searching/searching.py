# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code

   return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty

  elif len(arr) == 1:
    if arr[0] == target:
      return 0
    else:
      return -1  
  
  else:
    middle_index = len(arr)-1
    while middle_index > 0 and middle_index < len(arr):
      print(middle_index)
      if target == arr[middle_index]:
        return middle_index
      elif target > arr[middle_index]:
        middle_index = (middle_index+len(arr))//2
      else:
        middle_index = middle_index//2



  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2
  # print(middle)
  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  elif len(arr) == 1:
    if arr[0] == target:
      return 0
    else:
      return -1
  elif len(arr) == 2:
    if arr[0] == target:
      return 0
    if arr[1] == target:
      return 1
    else:
      return -1
  else:
    if target == middle:
      return middle
    elif target > middle:
      binary_search_recursive(arr, target, low, middle)
    else:
      binary_search_recursive(arr, target, middle, high)
