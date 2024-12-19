from collections import defaultdict
from math import inf
from typing import List

# '''
# Part 1
# '''
# def perform_operations(operations: List[str])->List[str]:  # type: ignore
#     output = []

#     db = defaultdict(list)

#     for operation in operations:
#         time, op, ID = operation.split(',') # be careful to what is the split criterion 
#         if not db[ID]:
#             if op == 'start':
#                 db[ID] = [int(time), inf] # need to parse str to int
#                 output.append('')
#             if op == 'check':
#                 output.append('inactive')
#             # if op == 'end': meaningless?
#         else:
#             if op == 'start':
#                 db[ID][0] = int(time)
#                 db[ID][1] = inf
#                 output.append('')
#             if op == 'end':
#                 db[ID][1] = int(time)
#                 output.append('')
#             if op == 'check':
#                 if db[ID][0] <= int(time) <= db[ID][1]:
#                     output.append('active')
#                 else:
#                     output.append('inactive')

#     return output

# operations1 = ['1,start,Michael', '5,check,Michael', '10,end,Michael', '15,check,Michael']
# print(f'input: {operations1}')
# print(f'output: {perform_operations(operations1)}') # expected output ['', 'active', '', 'inactive']

# operations2 = ['1,start,Michael', '3,check,Michael', '10,check,Angela']
# print(f'input: {operations2}')
# print(f'output: {perform_operations(operations2)}') # expected output ['', 'active', 'inactive']

'''
Part 2: potential 'duration' field
'''
def perform_operations(operations: List[str])->List[str]:  # type: ignore
    output = []

    db = defaultdict(list)

    for operation in operations:
        info = operation.split(',') # be careful to what is the split criterion 
        
        time = int(info[0])
        op = info[1]
        ID = info[2]
        end = inf
        if len(info) == 4:
            end = time + int(info[3])

        if not db[ID]:
            if op == 'start':
                db[ID] = [time, end] # need to parse str to int
                output.append('')
            if op == 'check':
                output.append('inactive')
            # if op == 'end': meaningless?
        else:
            if op == 'start':
                db[ID][0] = time
                db[ID][1] = end
                output.append('')
            if op == 'end':
                db[ID][1] = time
                output.append('')
            if op == 'check':
                if db[ID][0] <= time <= db[ID][1]:
                    output.append('active')
                else:
                    output.append('inactive')

    return output

operations1 = ['1,start,Michael,9', '10,check,Michael', '11,check,Michael']
print(f'input: {operations1}')
print(f'output: {perform_operations(operations1)}') # expected output ['', 'active', 'inactive']

operations2 = ['1,start,Michael', '2,start,Michael,5', '10,check,Michael']
print(f'input: {operations2}')
print(f'output: {perform_operations(operations2)}') # expected output ['', '', 'inactive']

'''
Part 3: potential 'duration' field, but no override
'''
# def perform_operations(operations: List[str])->List[str]:  # type: ignore
#     output = []

#     db = defaultdict(list)

#     for operation in operations:
#         info = operation.split(',') 
        
#         time = int(info[0])
#         op = info[1]
#         ID = info[2]

#         if not db[ID]:
#             if op == 'start':
#                 db[ID] = [time, time+int(info[3])] if len(info) == 4 else [time, inf]
#                 output.append('')
#             if op == 'check':
#                 output.append('inactive')
#             # if op == 'end': meaningless?
#         else:
#             if op == 'start':
#                 db[ID][0] = time
#                 if len(info) == 4:
#                     db[ID][1] = inf if db[ID][1] == inf else db[ID][1] + int(info[3])
#                 output.append('')
#             if op == 'end':
#                 db[ID][1] = time
#                 output.append('')
#             if op == 'check':
#                 if db[ID][0] <= time <= db[ID][1]:
#                     output.append('active')
#                 else:
#                     output.append('inactive')

#     return output

# operations1 = ['1,start,Michael,10', '2,start,Michael,4', '12,check,Michael']
# print(f'input: {operations1}')
# print(f'output: {perform_operations(operations1)}') # expected output ['', '', 'active']

# operations2 = ['1,start,Angela', '3,check,Angela', '5,start,Angela,10', '20,check,Angela']
# print(f'input: {operations2}')
# print(f'output: {perform_operations(operations2)}') # expected output ['', 'active', '', 'active']