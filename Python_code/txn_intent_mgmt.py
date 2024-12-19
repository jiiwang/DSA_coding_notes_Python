from collections import defaultdict
from math import inf

account_dict = defaultdict(list)
txn_dict = defaultdict(list)

'''
Part 1: Core features
'''
# def process_txn(filename:str)->str:
#     with open(filename, 'r', encoding='utf-8') as file:
#         for line in file:
#             # line will include the newline character at the end
#             # Use line.strip() to remove whitespace and newline
#             command = line.strip().split(' ')
#             op = command[0]

#             if op == 'START':
#                 account_dict[command[1]] = [int(num) for num in command[2:]]
#             elif op == 'NEW':
#                 txn_dict[command[1]] = [command[2], int(command[3]), 'PENDING']
#             elif op == 'PROCESS':
#                 txn_dict[command[1]][2] = 'IN_PROGRESS'
#             else:
#                 txn_dict[command[1]][2] = 'DONE'
#                 account_dict[txn_dict[command[1]][0]][0] += txn_dict[command[1]][1]
    
#     output = []
#     for account, balance in account_dict.items():
#         output.append(account + ' ' + str(balance[0]))
#
#     output.sort()
#     return output

# filename = 'Python_code/txn_intent_mgmt_1.txt'
# print(process_txn(filename)) # expected output = 'account1 50'

'''
Part 2: Extended features
'''
# def process_txn(filename:str)->str:
#     with open(filename, 'r', encoding='utf-8') as file:
#         for line in file:
#             # line will include the newline character at the end
#             # Use line.strip() to remove whitespace and newline
#             command = line.strip().split(' ')
#             op = command[0]

#             if op == 'START':
#                 account_dict[command[1]] = [int(num) for num in command[2:]]
#             elif op == 'NEW':
#                 txn_dict[command[1]] = [command[2], int(command[3]), 'PENDING']
#             elif op == 'MODIFY':
#                 if txn_dict[command[1]][2] == 'PENDING':
#                     txn_dict[command[1]][1] = int(command[2])  
#             elif op == 'PROCESS':
#                 txn_dict[command[1]][2] = 'IN_PROGRESS'
#             elif op == 'CANCEL':
#                 if txn_dict[command[1]][2] == 'IN_PROGRESS':
#                    txn_dict[command[1]][2] == 'PENDING'; 
#             elif op == 'COMPLETE':
#                 txn_dict[command[1]][2] = 'DONE'
#                 account_dict[txn_dict[command[1]][0]][0] += txn_dict[command[1]][1]
#             else:
#                 if txn_dict[command[1]][2] == 'DONE':
#                     txn_dict[command[1]][2] = 'REFUNDED'
#                     account_dict[txn_dict[command[1]][0]][0] -= txn_dict[command[1]][1]
    
#     output = []
#     for account, balance in account_dict.items():
#         output.append(account + ' ' + str(balance[0]))

#     output.sort()
#     return output

# filename = 'Python_code/txn_intent_mgmt_2.txt'
# print(process_txn(filename)) # expected output = ['account1 0', 'account2 35']

'''
Part 3: Time-limited refunds
'''
def process_txn(filename:str)->str:
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # line will include the newline character at the end
            # Use line.strip() to remove whitespace and newline
            command = line.strip().split(' ')
            time = int(command[0])
            op = command[1]

            if op == 'START':
                account_dict[command[2]].append(int(command[3]))
                if len(command) > 4:
                    account_dict[command[2]].append(time+int(command[4]))
                else:
                    account_dict[command[2]].append(inf)
            elif op == 'NEW':
                txn_dict[command[2]] = [command[3], int(command[4]), 'PENDING']
            elif op == 'MODIFY':
                if txn_dict[command[2]][2] == 'PENDING':
                    txn_dict[command[2]][1] = int(command[3])  
            elif op == 'PROCESS':
                txn_dict[command[2]][2] = 'IN_PROGRESS'
            elif op == 'CANCEL':
                if txn_dict[command[2]][2] == 'IN_PROGRESS':
                   txn_dict[command[2]][2] == 'PENDING'; 
            elif op == 'COMPLETE':
                txn_dict[command[2]][2] = 'DONE'
                account_dict[txn_dict[command[2]][0]][0] += txn_dict[command[2]][1]
            else:
                if txn_dict[command[2]][2] == 'DONE' and time <= account_dict[txn_dict[command[2]][0]][1]:
                    txn_dict[command[2]][2] = 'REFUNDED'
                    account_dict[txn_dict[command[2]][0]][0] -= txn_dict[command[2]][1]
    
    output = []
    for account, balance in account_dict.items():
        output.append(account + ' ' + str(balance[0]))

    output.sort()
    return output

filename = 'Python_code/txn_intent_mgmt_3.txt'
print(process_txn(filename)) # expected output = ['account1 0']