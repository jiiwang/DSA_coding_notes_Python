from collections import defaultdict

from typing import List

# def binarysearch_dict(dict:defaultdict, target:int)->int:
#     lo = 0
#     hi = target-dict[0]
	
#     # while lo <= hi:
#     #     mid = (lo+hi)//2
#     #     if not dict[mid]:
#     #         hi = mid-1 
#     #     elif dict[mid] == target:
#     #         return mid
#     #     elif dict[mid] < target:
#     #         lo = mid+1
#     #     else:
#     #         hi = mid-1
	
#     # return -1

#     # print(f"lo = {lo}, hi = {hi}")

#     while lo <= hi:
#         mid = (lo+hi)//2
#         # print(f"lo = {lo}, mid = {mid}, hi = {hi}")
#         if dict[mid] and dict[mid] < target:
#             lo = mid+1 
#         else:
#             hi = mid-1
	
#     print(f"lo = {lo}")
    
#     return lo if target == dict[lo] else -1

# def binarysearch_dict(dict:defaultdict, target:int)->int:
#     lo, hi = 0, target - dict[0]

#     while True:
#         if dict[hi] and target > dict[hi]:
#             hi = (hi-lo)*2 + lo
#         else:
#             break


#     while lo <= hi:
#        mid = (lo+hi)//2
#        # print(f"lo = {lo}, mid = {mid}, hi = {hi}")
#        if dict[mid] and dict[mid] < target:
#            lo = mid+1
#        else:
#            hi = mid-1
  
#     # print(f"lo = {lo}")
#     return lo if target == dict[lo] else -1

# dict = defaultdict(int)

# dict[0] = 1
# dict[1] = 1
# dict[1] = 1
# dict[2] = 1
# dict[3] = 2
# dict[4] = 2
# dict[5] = 3

# target = 2

# print(binarysearch_dict(dict, target))

def find_first_occur(a: List[int], target:int):
    lo, hi = 0, len(a)-1

    while lo <= hi:        
        mid = (lo+hi)//2
        # print(f"lo = {lo}, mid = {mid}, hi = {hi}")
        if a[mid] < target:
            lo = mid+1
        else:
            hi = mid-1

    lower = lo
    
    lo, hi = 0, len(a)-1

    while lo <= hi:        
        mid = (lo+hi)//2
        # print(f"lo = {lo}, mid = {mid}, hi = {hi}")
        if a[mid] <= target:
            lo = mid+1
        else:
            hi = mid-1
    
    upper = hi

    return (lower, upper) if lower <= len(a)-1 and a[lower] == target else -1

# test case
a = [1, 3, 8, 10, 10, 10, 13, 15]

target = 15

print(f"input: {a}")
print(f"first occurrence of {target}: {find_first_occur(a, target)}")