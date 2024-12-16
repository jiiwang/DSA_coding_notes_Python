# a = [1, 2, 3, 5]
# print(a[:3])

# import heapq

# twokey_heap = [(50, 0), (50, 2), (30, 3)]

# # sort by the first element in the tuplet, then the second
# heapq.heapify(twokey_heap)
# print(f"min heap top: {twokey_heap[0]}")

# heapq.heappush(twokey_heap, (20, 3))
# while twokey_heap:
#     print(f"visiting: {heapq.heappop(twokey_heap)}")

# class TreeNode:
#     def __init__(self, value=0, weight=0, left=None, right=None):
#         self.value = value
#         self.weight = weight
#         self.left = left
#         self.right = right

# def min_cost_remove_leaves(root):
#     def dfs(node):
#         if not node:
#             return 0
        
#         if not node.left and not node.right:
#             return node.weight

#         # Cost to remove left and right subtrees
#         left_cost = dfs(node.left)
#         right_cost = dfs(node.right)

#         # Current node cost plus cost of removing both subtrees
#         total_cost = left_cost + right_cost + node.weight

#         return total_cost

#     if not root:
#         return 0

#     return dfs(root)

# # Example usage:
# # Constructing a binary tree
# #          (5)
# #         /   \
# #       (3)   (7)
# #       /       \
# #     (1)       (4)

# leaf1 = TreeNode(value=1, weight=1)
# leaf2 = TreeNode(value=4, weight=4)
# left = TreeNode(value=3, weight=3, left=leaf1)
# right = TreeNode(value=7, weight=7, right=leaf2)
# root = TreeNode(value=5, weight=5, left=left, right=right)

# result = min_cost_remove_leaves(root)
# print("Minimum cost to remove all leaves:", result)

# """
# given the root of a tree, delete the tree
# """
# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right

# def deleteTree(root):
#     if root:
#         # delete left subtree
#         deleteTree(root.left)
#         # delete right subtree
#         deleteTree(root.right)
#         # traverse root
#         print("Deleting Node:", root.value)
#         del root

# # Example usage:
# # Constructing a binary tree
# #          (5)
# #         /   \
# #       (3)   (7)
# #       /       \
# #     (1)       (4)

# leaf1 = TreeNode(value=1)
# leaf2 = TreeNode(value=4)
# left = TreeNode(value=3, left=leaf1)
# right = TreeNode(value=7, right=leaf2)
# root = TreeNode(value=5, left=left, right=right)
# print(root.value)

# deleteTree(root)

# print(-25%26)

# sequential structure (list/string) slicing
# s = 'vrounbr'
# i = 3
# print(s[i::-1])
# print(s[:i:-1])

s = 'b'
print(int(s)-int('a'))