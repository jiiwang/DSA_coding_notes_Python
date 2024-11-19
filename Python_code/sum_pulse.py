"""
Google phone interview question

Given two lists of tuples where tuple has the form of (time=i, value=v) where
the tuple indicates that the value remains v from time i until time in the next tuple                           (1)

You can imagine these two lists as "pulse". 

Your task is to calculate the sum of two pulses,
return a list of the same format that satisfies (1)

Example:

t1 = [(0,0),(2,1),(8,0)]
t2 = [(0,0),(1,3),(5,2)]
the expected output ts = [(0,0),(1,3),(2,4),(5,3),(8,2)]

"""

from typing import List

def sum_two_pulses(t1: List[tuple], t2: List[tuple])->List[tuple]:
    m = len(t1)
    n = len(t2)

    ts = []

    ptr1 = ptr2 = 0

    prev1 = prev2 = 0

    curr = -1

    while ptr1 < m and ptr2 < n:
        print(f"ptr1 = {ptr1} and ptr2 = {ptr2}")
        if t1[ptr1][0] < t2[ptr2][0]:
            new_value = t1[ptr1][1] + t2[prev2][1]
            print(f"new_value = {new_value}")
            if not ts or (ts and new_value != ts[-1][1]):
                ts.append((t1[ptr1][0], new_value))
            prev1 = ptr1
            ptr1 += 1

        elif t1[ptr1][0] > t2[ptr2][0]:
            new_value = t1[prev1][1] + t2[ptr2][1]
            print(f"new_value = {new_value}")
            if not ts or (ts and new_value != ts[-1][1]):
                ts.append((t2[ptr2][0], new_value))
            prev2 = ptr2
            ptr2 += 1

        else:
            new_value = t1[ptr1][1] + t2[ptr2][1]
            print(f"new_value = {new_value}")
            if not ts or (ts and new_value != ts[-1][1]):
                ts.append((t1[ptr1][0], new_value))
            prev1 = ptr1
            ptr1 += 1
            prev2 = ptr2
            ptr2 += 1


    if ptr1 == m:
        ts.extend([(t2[i][0], t2[i][1] + t1[-1][1]) for i in range(ptr2,n)])
    
    if ptr2 == n:
        ts.extend([(t1[i][0], t1[i][1] + t2[-1][1]) for i in range(ptr1,m)])

    return ts

# test case
# t1 = [(0,0),(2,1),(8,0)]
# t2 = [(0,0),(1,3),(5,2)]

# print(f"first pulse is: {t1}")
# print(f"second pulse is: {t2}")
# print(f"sum of two pulses is: {sum_two_pulses(t1, t2)}")    # expected output is [(0,0),(1,3),(2,4),(5,3),(8,2)]

t1 = [(0,0),(1,1),(2,4),(8,0)]
t2 = [(0,3),(1,2),(5,3)]

print(f"first pulse is: {t1}")
print(f"second pulse is: {t2}")
print(f"sum of two pulses is: {sum_two_pulses(t1, t2)}")    # expected output is [(0,1),(2,6),(5,7),(8,3)]