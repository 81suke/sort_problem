from sort_core import swap

#
# SELECTION SORT
#
# IN:  arbitrary array
# OUT: array with all values sorted in increasing order
#
# METHOD:
# conceptually, consider two arrays: sorted, unsorted
# initially,
#   sorted   = []
#   unsorted = array
# iteratively,
#   remove the smallest element of unsorted
#   add it at the end of sorted
#
# NB: in the code below, index i represents the "border"
# between sorted and unsorted.
#

def sort(array):
    """ Non-destructive bubblesort sort.    
    array is unchanged; returns a sorted copy
    """
    res = array.copy()
    sort_inline(res)
    return res


def sort_inline(array):
    """ Inline selection sort.
    modifies the input array directly
    """
    # TODO: implement selection sort
    # replace the lines below with your own code
    n = len(array)
    for i in range(n-1):
        j = i
        for x in range(i + 1, n):
            if array[x] < array[j]:
                j = x
        k = array[i]
        array[i] = array[j]
        array[j] = k
    return array

