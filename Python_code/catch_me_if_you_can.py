# Define the function to solve the problem
def detect_fraudulent_merchants(approved_codes, fraudulent_codes, thresholds_table, merchants_table, min_transactions, charges_table):
    # Parse inputs
    approved_set = set(approved_codes.split(','))
    fraudulent_set = set(fraudulent_codes.split(','))

    # Parse thresholds
    thresholds = {}
    for row in thresholds_table.strip().split('\n'):
        mcc, threshold = row.split(',')
        thresholds[mcc] = int(threshold)

    # Parse merchants and their MCCs
    merchants = {}
    for row in merchants_table.strip().split('\n'):
        account_id, mcc = row.split(',')
        merchants[account_id] = mcc

    # Parse charges and track transactions
    transaction_counts = {}
    fraudulent_counts = {}

    for row in charges_table.strip().split('\n'):
        parts = row.split(',')
        if parts[0] != 'CHARGE':
            continue

        _, charge_id, account_id, amount, code = parts

        # Initialize transaction data for the account if not already present
        if account_id not in transaction_counts:
            transaction_counts[account_id] = 0
            fraudulent_counts[account_id] = 0

        # Increment total transactions
        transaction_counts[account_id] += 1

        # Increment fraudulent transactions if the code is in the fraudulent set
        if code in fraudulent_set:
            fraudulent_counts[account_id] += 1

    # Determine fraudulent merchants
    fraudulent_merchants = []

    for account_id, total_transactions in transaction_counts.items():
        # Skip if the merchant hasn't met the minimum transaction requirement
        if total_transactions < int(min_transactions):
            continue

        # Check if the fraudulent transactions exceed the threshold for the merchant's MCC
        mcc = merchants[account_id]
        fraud_threshold = thresholds[mcc]

        if fraudulent_counts[account_id] >= fraud_threshold:
            fraudulent_merchants.append(account_id)

    # Return a lexicographically sorted, comma-separated list of fraudulent merchants
    return ','.join(sorted(fraudulent_merchants))

# Example Input
approved = "approved,invalid_pin,expired_card"
fraudulent = "do_not_honor,stolen_card,lost_card"
thresholds = "retail,5\nairline,2\nvenue,3"
merchants = "acct_1,airline\nacct_2,venue\nacct_3,retail"
min_transactions = "0"
charges = """
CHARGE,ch_1,acct_1,100,do_not_honor
CHARGE,ch_2,acct_1,200,approved
CHARGE,ch_3,acct_1,300,do_not_honor
CHARGE,ch_4,acct_2,100,lost_card
CHARGE,ch_5,acct_2,200,lost_card
CHARGE,ch_6,acct_2,300,lost_card
CHARGE,ch_7,acct_3,100,lost_card
CHARGE,ch_8,acct_2,200,stolen_card
CHARGE,ch_9,acct_3,100,approved
"""

# Call the function and print the output
output = detect_fraudulent_merchants(approved, fraudulent, thresholds, merchants, min_transactions, charges)
print(output)




# input1 = ['approved', 'invalid_pin', 'expired_card']
# input2 = ['do_not_honor', 'stolen_card', 'lost_card']
# input3 = 'retail,5 \n airline,2 \n restaurant,10 \n venue,3'
# input4 = 'acct_1,airline \n acct_2,venue \n acct_3,retail'
# input5 = 0
# input6 = 'CHARGE,ch_1,acct_1,100,do_not_honor \n \
#           CHARGE,ch_2,acct_1,200,approved \n \
#           CHARGE,ch_3,acct_1,300,do_not_honor \n \
#           CHARGE,ch_4,acct_2,100,lost_card \n \
#           CHARGE,ch_5,acct_2,200,lost_card \n \
#           CHARGE,ch_6,acct_2,300,lost_card \n \
#           CHARGE,ch_7,acct_3,100,lost_card \n \
#           CHARGE,ch_8,acct_2,200,stolen_card \n \
#           CHARGE,ch_9,acct_3,100,approved'

# # expected output = 'acct_1,acct_2'