from typing import List

def swap(i: int, j: int, list: List):
    list[j], list[i] = list[i], list[j]

def leftzero_rightone(list: List)->List:
    if list is None:
        return list
	
    n = len(list)

    left, right = 0, n-1 
	
    while left <= right:
        if list[left] == 0:
            left+=1	
		
        else:
            swap(left, right, list)
            right-=1

    return list

# list1 = [1, 0, 1, 0, 1, 1 ,1, 1, 0]
# print(leftzero_rightone(list1))

def partition(list: List[int])->List[int]:
    if list is None or len(list) == 1:
        return list
	
    n = len(list)

    pivot = list[0]
	
    left, right = 1, n-1
	
    # beware of the condition <=, think why < doesn't work
    # if termination is <,
    # then after the while loop, left == right
    # however list[left] might still be < pivot, counter should still increment
    while left <= right:
        # print(left, right)
        # print(list)
    
        if list[left] <= pivot:
            left+=1	
		
        else:
            swap(left, right, list)
            right-=1

    # print("after all but 1 swap: ",left, right)
	
    swap(0, left-1, list)

    return list

print('------Test case 1---------')
list2 = [6, 3, 8, 9, 5, 7, 12]
print("before quick sort: ", list2)
print("after finding the position of the pivot: ", partition(list2))

# print('------Test case 2---------')
# list3 = [23, 4, 12, 67, 89, 34, 1]
# print("before quick sort: ", list3)
# print("after finding the position of the pivot: ", partition(list3))

print('------Test case 3---------')
list4 = [15, 12, 9, 6, 3, 1]
print("before quick sort: ", list4)
print("after finding the position of the pivot: ", partition(list4))

