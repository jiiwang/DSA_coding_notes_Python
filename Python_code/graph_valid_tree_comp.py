import time
import random

# Helper function to generate edges for a graph with n nodes
def generate_edges(n, is_tree=True):
    edges = []
    for i in range(1, n):
        edges.append((i - 1, i))
    if not is_tree:
        extra_edges = [(random.randint(0, n-1), random.randint(0, n-1)) for _ in range(n // 2)]
        edges.extend(extra_edges)
    return edges

# Union-Find base class
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, p):
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p != root_q:
            self.parent[root_p] = root_q

# Union-Find with Path Compression
class UnionFindPathCompression:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, p):
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p != root_q:
            self.parent[root_p] = root_q

# Union-Find with Union by Size and Path Compression
class UnionFindBySize:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, p):
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p != root_q:
            if self.size[root_p] < self.size[root_q]:
                self.parent[root_p] = root_q
                self.size[root_q] += self.size[root_p]
            else:
                self.parent[root_q] = root_p
                self.size[root_p] += self.size[root_q]

# Function to check if the given graph is a valid tree
def is_valid_tree(n, edges, uf_class):
    if len(edges) != n - 1:
        return False
    uf = uf_class(n)
    for u, v in edges:
        if uf.find(u) == uf.find(v):
            return False
        uf.union(u, v)
    return True

# Running the tests
n = 10000
trials = 100
edges = generate_edges(n)

implementations = [
    ("Basic Union-Find", UnionFind),
    ("Union-Find with Path Compression", UnionFindPathCompression),
    ("Union-Find with Union by Size and Path Compression", UnionFindBySize)
]

for name, uf_class in implementations:
    start_time = time.time()
    for j in range(trials):
        result = is_valid_tree(n, edges, uf_class)
    end_time = time.time()
    print(f"{name}: Time taken = {(end_time - start_time)/trials:.6f} seconds, Result = {result}")