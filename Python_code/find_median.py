# find median of a list (unsorted)
# for simplity, assume the list have odd number length
def swap(l, i, j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp

def findLoc(l, i, j):
    pivot = l[i]
    
    for k in range(i+1, j+1):
        if l[k] < pivot:
            swap(l, i, k)
            i+=1
        
    if l[i] != pivot:
        swap(l, i, j)
    
    return i

def findMedian(l):
    n = len(l)
    target = int(n/2)

    i, j = 0, n-1
    while i <= j:
        k = findLoc(l, i, j)
        if k < target:
            i = k+1
        elif k == target:
            return l[k]
        else:
            j = k-1
    
l = [1,5,3,2,8,9,6]
print(findMedian(l))
