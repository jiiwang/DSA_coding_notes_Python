from collections import defaultdict
from math import inf
from typing import List


def perform_operations(operations: List[str])->List[str]:  # type: ignore
    output = []

    db = defaultdict(list)

    for operation in operations:
        time, op, ID = operation.split(', ') # be careful to what is the split criterion 
        if not db[ID]:
            if op == 'start':
                db[ID] = [int(time), inf] # need to parse str to int
                output.append('')
            if op == 'check':
                output.append('inactive')
            # if op == 'end': meaningless?
        else:
            if op == 'start':
                db[ID][0] = int(time)
                db[ID][1] = inf
                output.append('')
            if op == 'end':
                db[ID][1] = int(time)
                output.append('')
            if op == 'check':
                if db[ID][0] <= int(time) <= db[ID][1]:
                    output.append('active')
                else:
                    output.append('inactive')

    return output

operations = ['1, start, Michael', '5, check, Michael', '10, end, Michael', '15, check, Michael']
print(f'input: {operations}')
print(f'output: {perform_operations(operations)}') # expected output ['', 'active', '', 'inactive']