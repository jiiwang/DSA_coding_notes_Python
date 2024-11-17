from collections import defaultdict

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

def binarysearch_dict(dict:defaultdict, target:int)->int:
    lo, hi = 0, target - dict[0]

    while True:
        if dict[hi] and target > dict[hi]:
            hi = (hi-lo)*2 + lo
        else:
            break


    while lo <= hi:
       mid = (lo+hi)//2
       # print(f"lo = {lo}, mid = {mid}, hi = {hi}")
       if dict[mid] and dict[mid] < target:
           lo = mid+1
       else:
           hi = mid-1
  
    # print(f"lo = {lo}")
    return lo if target == dict[lo] else -1

dict = defaultdict(int)

dict[0] = 1
dict[1] = 1
dict[1] = 1
dict[2] = 1
dict[3] = 2
dict[4] = 2
dict[5] = 3

target = 2

print(binarysearch_dict(dict, target))