from typing import List

def combinations_with_sum_ge_k(nums, k):
    result = []
    n = len(nums)
    
    # Helper function to generate combinations
    def generate_combinations(start, current_comb, sum):
        if sum >= k:
            result.append(current_comb[:])  # need to make a copy
            if len(current_comb) == n:
                return
            
        for i in range(start, n):
            current_comb.append(i)
            # sum += nums[i]
            generate_combinations(i + 1, current_comb, sum+nums[i])
            # sum -= nums[i]
            current_comb.pop()
    
    # Generate all combinations
    generate_combinations(0, [], 0)
    return result

# test case
a = [3,6,1]
target = 5

print(f"input array: \n{a}")
print(f"target: {target}")
print(f"combinations whose sum >= target: \n {combinations_with_sum_ge_k(a, target)}")

