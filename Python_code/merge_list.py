from typing import List
import heapq
import random

def merge_two_list(list1: List[int], list2: List[int])->List[int]:
	m = len(list1)
	n = len(list2)
	
	merged_list = [0]*(m+n)
    	
	i, j, k = 0, 0, 0
	
	while i < m and j < n:
		if list1[i] < list2[j]:
			merged_list[k] = list1[i]
			k+=1
			i+=1
		else:
			merged_list[k] = list2[j]
			k+=1
			j+=1

	if i == m and j < n:
		while j < n:
			merged_list[k] = list2[j]
			k+=1
			j+=1

	if j == n and i < m:
		while i < m:
			merged_list[k] = list1[i]
			k+=1
			i+=1

	return merged_list

# list1 = [1, 3, 8, 10]
# list2 = [2, 4, 7, 12, 13, 18]
# print(merge_two_list(list1, list2))

def merge_lists(list: List[List[int]])->List[int]:
	m = len(list)
	n = len(list[0])
	
	heap = [0]*(m*n)

	for i in range(m):
		for j in range(n):
			heap[i*n+j] = list[i][j]

	heapq.heapify(heap)
	
	ans = [0]*(m*n)
	k = 0

	while heap:
		ans[k] = heapq.heappop(heap)
		k += 1

	return ans

# list = [3,9,7]
list = [[1, 3, 8, 10],[2, 4, 7, 12]]

print(merge_lists(list))

def generate_random_matrix(m: int, n: int)->List[List[int]]:
    return [[random.randint(0, 100) for _ in range(n)] for _ in range(m)]

m, n = 6, 10

matrix = generate_random_matrix(m, n)

print(matrix)

print(merge_lists(matrix))
