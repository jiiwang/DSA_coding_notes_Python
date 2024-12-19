from collections import defaultdict

account_dict = defaultdict(list)
txn_dict = defaultdict(list)

def process_txn(filename:str)->str:
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # line will include the newline character at the end
            # Use line.strip() to remove whitespace and newline
            command = line.strip().split(' ')
            op = command[0]

            if op == 'START':
                account_dict[command[1]] = [int(num) for num in command[2:]]
            elif op == 'NEW':
            
            elif op == 'PROCESS':
            
            else:

    output = ''

    return output

# input = 'START account1 0\n \
# NEW txn1 account1 50\n \
# PROCESS txn1\n \
# COMPLETE txn1'
# expected output = 'account1 50'
filename = 'Python_code/txn_intent_mgmt.txt'
process_txn(filename)