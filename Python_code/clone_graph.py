# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: Node) -> Node:
    if not node:
        return None

    # hashmap: key is old, value is copy
    # purpose: keep track of visited nodes and avoid creating duplicate copies
    # reflection: why don't we use ``set"
    old_to_new = {}

    def dfs(node: Node):
        # no need to make a copy
        if node in old_to_new:
            return old_to_new[node]
        else:
            copy_node = Node(node.val)
            old_to_new[node] = copy_node
            for neighbor in node.neighbors:
                copy_node.neighbors.append(dfs(neighbor))
            return copy_node
    
    return dfs(node)

# test case
# 1 ----- 2
# |       |
# |       |
# 3 ----- 4
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node3]
node2.neighbors = [node1, node4]
node3.neighbors = [node1, node4]
node4.neighbors = [node2, node3]

print("---make a copy---")
print(f"node 1: {node1}")

copy_node1 = cloneGraph(node1)
print(f"copy of node 1: {copy_node1}")

print(f"neighbors of node 1: {node1.neighbors}")
print(f"neighbors of the copy of node 1: {copy_node1.neighbors}")