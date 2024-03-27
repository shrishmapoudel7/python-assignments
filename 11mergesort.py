def merge_sort(arr):
    if len(arr) > 1:  # Corrected condition from len>1 to len(arr) > 1
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # Recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Merge
        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1      #The purpose of incrementing k is to ensure that we fill the merged array in order without overwriting any elements that have already been placed.

        # Copy the remaining elements of left_arr, if any
        while i < len(left_arr):
            arr[k] = left_arr[i]    #comp ni garna paryo
            i += 1
            k += 1

        # Copy the remaining elements of right_arr, if any
        while j < len(right_arr):        #comp ni garna paryo
            arr[k] = right_arr[j]
            j += 1
            k += 1


# Test the function
arr_test = [2, 3, 5, 1, 7, 4, 4, 2, 6, 0]
merge_sort(arr_test)
print(arr_test)
