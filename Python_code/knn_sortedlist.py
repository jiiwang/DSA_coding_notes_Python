import heapq
from typing import List

"""
Question:
given a sorted list, and a target,
return a list of k numbers from the sorted list that are the closest to the target
"""
def findknn(list: List[int], target:int, k:int)->List[int]:
    n = len(list)
	
    # corner case:
    if n < k:
        print("err msg: k is larger than the length of the list.")	
        return 

    if n == k:
        return list
	
    lo, hi = 0, n-1
	
	# binary search
    while lo <= hi:
        mid = (lo+hi)//2

        if target > list[mid]:
            lo = mid+1
        else:
            hi = mid-1
    
    # after binary search, we obtain lo such that
    # list[lo-1] < target <= list[lo]

    print(f"insertion idx: {lo}")

    if lo == 0:
        return list[:k]

    if lo == n:
        return list[-k:]
    
    """
    Solution 1: use heap, equiv to top k elements
    time complexity: O(logn + klogk)
    space complexity: O(k)
    """
    # should be max heap
    # gap_heap = []
    # for num in list[max(0, lo-k): min(n, lo+k)]:
    #     heapq.heappush(gap_heap, (-abs(num-target), num))

    #     if len(gap_heap) > k:
    #         heapq.heappop(gap_heap)

    # knn = []

    # while gap_heap:
    #     knn.append(heapq.heappop(gap_heap)[1])

    # return knn

    """
    Solution 2: two pointers
    time complexity: O(logn + k)
    space complexity: O(1)
    """
    l, r = lo-1, lo

    knn = [0]*k

    for i in range(k):
        print(f"l = {l}, r = {r}")
        if l >= 0 and (r > n-1 or (r <= n-1 and abs(list[l]-target) < abs(list[r] - target))):
            knn[i] = list[l]
            l-=1
        else:
            knn[i] = list[r]
            r+=1
          
    return knn

# test case
l1 = [1, 3, 9, 12, 15, 18]
target1 = 2
k = 4

print(f"input list\n {l1}")
print(f"target: {target1}")
print(f"{k}-nn of the input list\n {findknn(l1, target1, k)}")

