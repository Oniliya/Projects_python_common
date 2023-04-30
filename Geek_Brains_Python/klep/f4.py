# funtion to divide the lists in the two sublists 
def merge_sort(list1, left_index, right_index): 
    if left_index >= right_index: 
        return 
    middle = (left_index + right_index)//2 
    merge_sort(list1, left_index, middle) 
    merge_sort(list1, middle + 1, right_index) 
    merge(list1, left_index, right_index, middle) 
    print(left_index+1, right_index+1, list1[left_index], list1[right_index])
 
# Defining a function for merge the list 
def merge(list1, left_index, right_index, middle): 
 
    # Creating subparts of a lists 
    left_sublist = list1[left_index:middle + 1] 
    right_sublist = list1[middle+1:right_index+1] 
 
    # Initial values for variables that we use to keep 
    # track of where we are in each list1 
    left_sublist_index = 0 
    right_sublist_index = 0 
    sorted_index = left_index 
 
    # traverse both copies until we get run out one element 
    while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist): 
 
        # If our left_sublist has the smaller element, put it in the sorted 
        # part and then move forward in left_sublist (by increasing the pointer) 
        if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]: 
            list1[sorted_index] = left_sublist[left_sublist_index] 
            left_sublist_index = left_sublist_index + 1 
        # Otherwise add it into the right sublist 
        else: 
            list1[sorted_index] = right_sublist[right_sublist_index] 
            right_sublist_index = right_sublist_index + 1 
 
        # move forward in the sorted part 
        sorted_index = sorted_index + 1 
      
    # we will go through the remaining elements and add them 
    while left_sublist_index < len(left_sublist): 
        list1[sorted_index] = left_sublist[left_sublist_index] 
        left_sublist_index = left_sublist_index + 1 
        sorted_index = sorted_index + 1 
 
    while right_sublist_index < len(right_sublist): 
        list1[sorted_index] = right_sublist[right_sublist_index] 
        right_sublist_index = right_sublist_index + 1 
        sorted_index = sorted_index + 1 
 
# list1 = [44, 65, 2, 3, 58, 14, 57, 23, 10, 1, 7, 74, 48] 
list1 = [5, 4, 3, 2, 1]
print(list1)
merge_sort(list1, 0, len(list1) -1) 
print(list1) 































# import operator
# def merge_sort(L, compare=operator.lt):
#     if len(L) < 2:
#         return L[:]
#     else:
#         middle = int(len(L) / 2)
#         left = merge_sort(L[:middle], compare)
#         right = merge_sort(L[middle:], compare)
#         return merge(left, right, compare)
        

# def merge(left, right, compare):
#     result = []
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if compare(left[i], right[j]):
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result

# array = [78, 41, 4, 27, 3, 27, 8, 39, 19, 34, 6, 41, 13, 52, 16]
# print(array)
# print(merge_sort(array))
