# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index

        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             

        
        arr[i], arr[smallest_index] = arr[smallest_index],arr[i]
        print('smallest value:', arr[smallest_index])

        # TO-DO: swap

    return arr

ex = [9,8,7,6,5,4,3,2,1]
selection_sort(ex)
print(ex)


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr