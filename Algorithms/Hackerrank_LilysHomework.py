# Time Complexity: O(NlogN) due to sorting
# Space Complexity: O(N) create a dictionary to store the index

def lilysHomework(arr):
    asc_arr = sorted(arr)
    desc_arr = sorted(arr, reverse=True)

    return min(swap(arr, asc_arr), swap(arr, desc_arr))


def swap(arr, correct_arr):
    arr_copy = arr.copy()

    d = {arr[i]: i for i in range(len(arr))}

    swap_times = 0
    for i, ele in enumerate(arr_copy):
        correct_ele = correct_arr[i]

        if ele != correct_ele:
            arr_copy[i], arr_copy[d[correct_ele]] = arr_copy[d[correct_ele]], arr_copy[i]

            swap_times += 1

            d[ele], d[correct_ele] = d[correct_ele], d[ele]

    return swap_times

