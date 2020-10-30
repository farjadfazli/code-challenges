def binary_search(arr, target):
    min_idx = 0
    max_idx = len(arr) - 1

    while min_idx < max_idx:
        
        mid_idx = (min_idx + max_idx) // 2

        if target == arr[mid_idx]:
            return mid_idx
        
        elif arr[mid_idx] < target:
            min_idx = mid_idx + 1

        else:
            max_idx = mid_idx - 1

    return -1



example_arr = [3, 4, 6, 7, 12, 26, 90, 104]
example_target = 26

print(binary_search(example_arr, example_target))