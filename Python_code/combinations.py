from typing import List

def combinations(a:List[int], target:int)->List[List[int]]:
    n = len(a)
    comb = []

    def backtracking(sum:int, curr_idx:int, curr_comb:List[int]):
        print(f"sum: {sum}, curr_idx: {curr_idx}, curr_comb: {curr_comb}")
        if sum >= target:
            comb.append(curr_comb[:]) # copy is needed
            if len(curr_comb) == n:
                return
        
        curr_comb.append(curr_idx)
        for j in range(curr_idx, n):
            backtracking(sum+a[curr_idx], j, curr_comb)
        curr_comb.pop()        

    backtracking(0, 0, [])
    return comb

# test case
a = [3,6,1]
target = 5

print(f"input array: \n{a}")
print(f"target: {target}")
print(f"combinations whose sum >= target: \n {combinations(a, target)}")

