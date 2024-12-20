'''
Part 1: catch me if you can
'''

# # Define the function to solve the problem
# def detect_fraudulent_merchants(approved_codes, fraudulent_codes, thresholds_table, merchants_table, min_transactions, charges_table):
#     # Parse inputs
#     approved_set = set(approved_codes.split(','))
#     fraudulent_set = set(fraudulent_codes.split(','))

#     # Parse thresholds
#     thresholds = {}
#     for row in thresholds_table.strip().split('\n'):
#         mcc, threshold = row.split(',')
#         thresholds[mcc] = int(threshold)

#     # Parse merchants and their MCCs
#     merchants = {}
#     for row in merchants_table.strip().split('\n'):
#         account_id, mcc = row.split(',')
#         merchants[account_id] = mcc

#     # Parse charges and track transactions
#     transaction_counts = {}
#     fraudulent_counts = {}

#     for row in charges_table.strip().split('\n'):
#         parts = row.split(',')
#         if parts[0] != 'CHARGE':
#             continue

#         _, charge_id, account_id, amount, code = parts

#         # Initialize transaction data for the account if not already present
#         if account_id not in transaction_counts:
#             transaction_counts[account_id] = 0
#             fraudulent_counts[account_id] = 0

#         # Increment total transactions
#         transaction_counts[account_id] += 1

#         # Increment fraudulent transactions if the code is in the fraudulent set
#         if code in fraudulent_set and transaction_counts[account_id] > int(min_transactions):
#             fraudulent_counts[account_id] += 1

#     # Determine fraudulent merchants
#     fraudulent_merchants = []

#     for account_id, total_transactions in transaction_counts.items():
#         # Skip if the merchant hasn't met the minimum transaction requirement
#         if total_transactions <= int(min_transactions):
#             continue

#         # Check if the fraudulent transactions exceed the threshold for the merchant's MCC
#         mcc = merchants[account_id]
#         fraud_threshold = thresholds[mcc]

#         if fraudulent_counts[account_id] >= fraud_threshold:
#             fraudulent_merchants.append(account_id)

#     # Return a lexicographically sorted, comma-separated list of fraudulent merchants
#     return ','.join(sorted(fraudulent_merchants))

# # Example Input
# approved = "approved,invalid_pin,expired_card"
# fraudulent = "do_not_honor,stolen_card,lost_card"
# thresholds = "retail,5\nairline,2\nvenue,3"
# merchants = "acct_1,airline\nacct_2,venue\nacct_3,retail"
# min_transactions = "0"
# charges = """
# CHARGE,ch_1,acct_1,100,do_not_honor
# CHARGE,ch_2,acct_1,200,approved
# CHARGE,ch_3,acct_1,300,do_not_honor
# CHARGE,ch_4,acct_2,100,lost_card
# CHARGE,ch_5,acct_2,200,lost_card
# CHARGE,ch_6,acct_2,300,lost_card
# CHARGE,ch_7,acct_3,100,lost_card
# CHARGE,ch_8,acct_2,200,stolen_card
# CHARGE,ch_9,acct_3,100,approved
# """

# # Call the function and print the output
# output = detect_fraudulent_merchants(approved, fraudulent, thresholds, merchants, min_transactions, charges)
# print(output) # expected output = 'acct_1,acct_2'

'''
Part 2: if threshold is not an absolute value, but a ratio
'''
# # Define the function to solve the problem
# def detect_fraudulent_merchants(approved_codes, fraudulent_codes, thresholds_table, merchants_table, min_transactions, charges_table):
#     # Parse inputs
#     approved_set = set(approved_codes.split(','))
#     fraudulent_set = set(fraudulent_codes.split(','))

#     # Parse thresholds
#     thresholds = {}
#     for row in thresholds_table.strip().split('\n'):
#         mcc, threshold = row.split(',')
#         thresholds[mcc] = float(threshold)

#     # Parse merchants and their MCCs
#     merchants = {}
#     for row in merchants_table.strip().split('\n'):
#         account_id, mcc = row.split(',')
#         merchants[account_id] = mcc

#     # Parse charges and track transactions
#     transaction_counts = {}
#     fraudulent_counts = {}

#     for row in charges_table.strip().split('\n'):
#         parts = row.split(',')
#         if parts[0] != 'CHARGE':
#             continue

#         _, charge_id, account_id, amount, code = parts

#         # Initialize transaction data for the account if not already present
#         if account_id not in transaction_counts:
#             transaction_counts[account_id] = 0
#             fraudulent_counts[account_id] = 0

#         # Increment total transactions
#         transaction_counts[account_id] += 1

#         # Increment fraudulent transactions if the code is in the fraudulent set
#         if code in fraudulent_set and transaction_counts[account_id] > int(min_transactions):
#             fraudulent_counts[account_id] += 1

#     # Determine fraudulent merchants
#     fraudulent_merchants = []

#     for account_id, total_transactions in transaction_counts.items():
#         # Skip if the merchant hasn't met the minimum transaction requirement
#         if total_transactions <= int(min_transactions):
#             continue

#         # Check if the fraudulent transactions exceed the threshold for the merchant's MCC
#         mcc = merchants[account_id]
#         fraud_threshold = thresholds[mcc]

#         if fraudulent_counts[account_id] >= fraud_threshold*(total_transactions-int(min_transactions)):
#             fraudulent_merchants.append(account_id)

#     # Return a lexicographically sorted, comma-separated list of fraudulent merchants
#     fraudulent_merchants.sort()
#     return ','.join(fraudulent_merchants)

# # Example Input
# approved = "approved,invalid_pin,expired_card"
# fraudulent = "do_not_honor,stolen_card,lost_card"
# thresholds = "retail,0.5\nairline,0.25\nrestaurant,0.8\nvenue,0.25"
# merchants = "acct_1,airline\nacct_2,venue\nacct_3,venue"
# min_transactions = "2"
# charges = """
# CHARGE,ch_1,acct_1,100,do_not_honor
# CHARGE,ch_2,acct_1,200,approved
# CHARGE,ch_3,acct_1,300,do_not_honor
# CHARGE,ch_4,acct_2,400,approved
# CHARGE,ch_5,acct_2,500,approved
# CHARGE,ch_6,acct_1,600,lost_card
# CHARGE,ch_7,acct_2,700,approved
# CHARGE,ch_8,acct_2,800,approved
# CHARGE,ch_9,acct_3,800,approved
# CHARGE,ch_10,acct_3,700,approved
# CHARGE,ch_11,acct_3,600,approved
# CHARGE,ch_12,acct_3,500,stolen_card
# CHARGE,ch_13,acct_3,500,stolen_card
# CHARGE,ch_14,acct_2,400,stolen_card
# """

# # Call the function and print the output
# output = detect_fraudulent_merchants(approved, fraudulent, thresholds, merchants, min_transactions, charges)
# print(output) # expected output = 'acct_1,acct_2,acct_3'

'''
Part 3: Add DISPUTE function
'''
def detect_fraudulent_merchants(approved_codes, fraudulent_codes, thresholds_table, merchants_table, min_transactions, charges_table):
    # Parse inputs
    approved_set = set(approved_codes.split(','))
    fraudulent_set = set(fraudulent_codes.split(','))

    # Parse thresholds
    thresholds = {}
    for row in thresholds_table.strip().split('\n'):
        mcc, threshold = row.split(',')
        thresholds[mcc] = float(threshold)

    # Parse merchants and their MCCs
    merchants = {}
    for row in merchants_table.strip().split('\n'):
        account_id, mcc = row.split(',')
        merchants[account_id] = mcc

    # Parse charges and track transactions
    transaction_table = {}
    transaction_counts = {}
    fraudulent_counts = {}

    for row in charges_table.strip().split('\n'):
        parts = row.split(',')
        if parts[0] == 'CHARGE':
            _, charge_id, account_id, amount, code = parts

            transaction_table[charge_id] = (account_id, code)

            # Initialize transaction data for the account if not already present
            if account_id not in transaction_counts:
                transaction_counts[account_id] = 0
                fraudulent_counts[account_id] = 0

            # Increment total transactions
            transaction_counts[account_id] += 1

            # Increment fraudulent transactions if the code is in the fraudulent set
            if code in fraudulent_set and transaction_counts[account_id] > int(min_transactions):
                fraudulent_counts[account_id] += 1

        elif parts[0] == 'DISPUTE':
            _, charge_id = parts

            account_id, code = transaction_table[charge_id]

            if code in fraudulent_set and transaction_counts[account_id] > int(min_transactions):
                fraudulent_counts[account_id] -= 1
            
            transaction_table[charge_id] = (account_id, 'approved')

    # Determine fraudulent merchants
    fraudulent_merchants = []

    for account_id, total_transactions in transaction_counts.items():
        # Skip if the merchant hasn't met the minimum transaction requirement
        if total_transactions <= int(min_transactions):
            continue

        # Check if the fraudulent transactions exceed the threshold for the merchant's MCC
        mcc = merchants[account_id]
        fraud_threshold = thresholds[mcc]

        if fraudulent_counts[account_id] >= fraud_threshold*(total_transactions-int(min_transactions)):
            fraudulent_merchants.append(account_id)

    # Return a lexicographically sorted, comma-separated list of fraudulent merchants
    fraudulent_merchants.sort()
    return ','.join(fraudulent_merchants)

# Example Input
approved = "approved,invalid_pin,expired_card"
fraudulent = "do_not_honor,stolen_card,lost_card"
thresholds = "retail,0.8\nvenue,0.2"
merchants = "acct_1,retail\nacct_2,retail"
min_transactions = "2"
charges = """
CHARGE,ch_1,acct_1,100,do_not_honor
CHARGE,ch_2,acct_1,200,lost_card
CHARGE,ch_3,acct_1,300,do_not_honor
DISPUTE,ch_2
CHARGE,ch_4,acct_2,400,lost_card
CHARGE,ch_5,acct_2,500,lost_card
CHARGE,ch_6,acct_1,600,lost_card
CHARGE,ch_7,acct_2,700,lost_card
CHARGE,ch_8,acct_2,800,do_not_honor
"""

# Call the function and print the output
output = detect_fraudulent_merchants(approved, fraudulent, thresholds, merchants, min_transactions, charges)
print(output) # expected output = 'acct_2'