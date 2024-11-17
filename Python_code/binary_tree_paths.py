from typing import List

class TreeNode:
     def __init__(self, val = 0, left = None, right = None):
          self.val = val
          self.left = left
          self.right = right


def binaryTreePaths(root:TreeNode)->List[str]:
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    def construct_paths(root, path):
        if root:
            path += str(root.val)
            if not root.left and not root.right:  # if reach a leaf
                paths.append(path)  # update paths  
            else:
                path += '->'  # extend the current path
                construct_paths(root.left, path)
                construct_paths(root.right, path)

    paths = []
    construct_paths(root, '')
    return paths

# test cases
# Building a sample tree: 1 -> 2, 3 (2 -> 5)
#        1
#       / \
#      2   3
#       \
#        5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

print(binaryTreePaths(root))