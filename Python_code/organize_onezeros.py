import random
from typing import List

def generate_random_list(n):
    return [random.choice([-1, 0, 1]) for _ in range(n)]

def swap(i: int, j: int, list: List[int]):
    list[j], list[i] = list[i], list[j]

def leftnegone_midzero_rightone(list: List[int])->List[int]:
    if not list:
        return list
	
    n = len(list)

    '''
    Solution 1: two pass
    '''
    # left, right = 0, n-1 
    
    # while left <= right:
    #     if list[left] == 0 or list[left] == -1:
    #         left+=1	
		
    #     else:
    #         swap(left, right, list)
    #         right-=1

    # left = 0

    # while left <= right:
    #     if list[left] == -1:
    #         left+=1
    #     else:
    #         swap(left, right, list)
    #         right-=1

    '''
    Solution 2: one pass
    '''
    # left: pointer to -1
    # mid: current pointer
    # right: pointer to 1
    left, mid, right = 0, 0, n-1
    
    while mid <= right:
        if list[mid] == -1:
            swap(mid, left, list)
            left += 1
            mid += 1
        elif list[mid] == 0:
            mid += 1
        else:  # list[mid] == 1
            swap(right, mid, list)
            right -= 1   

    return list

# test case 1
# list1 = [-1, 0, 1, -1, -1, 1, 1, 1, 0]
# print(leftnegone_midzero_rightone(list1))

# other test case 
trial = 5
n = 10

for i in range(trial):
    print(f"-------test case {i+1}---------")
    l = generate_random_list(n)
    print("input list: \n", l)
    print("output list: \n", leftnegone_midzero_rightone(l))