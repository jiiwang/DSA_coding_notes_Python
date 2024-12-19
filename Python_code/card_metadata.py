from typing import List

'''
Part 1 and 2: No overlapping, extend to both ends
'''
# def card_metadata(input: str) -> List[str]:
#     lines = input.split('\n')
#     BIN = lines[0]
#     n = int(lines[1])

#     lower = '0'*10
#     upper = '9'*10
#     output = sorted(lines[2:])
#     output = [x.split(',') for x in output]

#     if n == 1:
#         output[0][0] = lower
#         output[0][1] = upper

#     else:
#         for i in range(n):
#             if i == 0:
#                 output[i][0] = lower
#                 output[i][1] = str(int(output[i+1][0]) - 1)
#             elif i == n-1:
#                 output[i][0] = str(int(output[i-1][1]) + 1)
#                 output[i][1] = upper
#             else:
#                 output[i][0] = str(int(output[i-1][1]) + 1)
#                 output[i][1] = str(int(output[i+1][0]) - 1)

#     return [BIN+y[0]+','+BIN+y[1]+','+y[2] for y in output]

# # input1 = '424242\n1\n5000000000,6555555555,VISA'
# # print(f'input: \n{input1}')
# # print(f'output: \n{card_metadata(input1)}') # expected output = ['4242420000000000,4242429999999999,VISA']

# # input2 = '424242\n2\n4000000000,8999999999,MASTERCARD\n1000000000,3999999999,VISA'
# # print(f'input: \n{input2}')
# # print(f'output: \n{card_metadata(input2)}') # expected output = ['4242420000000000,4242423999999999,VISA', '4242424000000000,4242429999999999,MASTERCARD']

# input1 = '424242\n2\n0000000000,3700000000,VISA\n6100000000,9999999999,MASTERCARD'
# print(f'input: \n{input1}')
# print(f'output: \n{card_metadata(input1)}') # expected output = ['4242420000000000,4242426099999999,VISA', '4242426100000000,4242429999999999,MASTERCARD']

# input2 = '424242\n3\n1000000000,1299999999,VISA\n1900000000,9999999999,AMEX\n1500000000,1699999999,MASTERCARD'
# print(f'input: \n{input2}')
# print(f'output: \n{card_metadata(input2)}') # expected output = ['4242420000000000,4242421499999999,VISA', '4242421500000000,4242421899999999,MASTERCARD', '4242421900000000,4242429999999999,AMEX']

'''
Part 3: contains intervals that are proper subsets of other intervals
'''
# def card_metadata(input: str) -> List[str]:
#     lines = input.split('\n')
#     BIN = lines[0]
#     n = int(lines[1])

#     lower = '0'*10
#     upper = '9'*10

#     intervals = sorted(lines[2:])
#     intervals = [x.split(',') for x in intervals]

#     # check proper subset, and delete if found
#     clean = [intervals[0]]

#     for interval in intervals:
#         start = int(interval[0])
#         end = int(interval[1])

#         if start == int(clean[-1][0]) and end >= int(clean[-1][1]):
#             clean[-1] = interval
#         elif start >= int(clean[-1][1]):
#             clean.append(interval)
#         else:
#             continue
    
#     m = len(clean)
#     if m == 1:
#         clean[0][0] = lower
#         clean[0][1] = upper

#     else:
#         for i in range(m):
#             if i == 0:
#                 clean[i][0] = lower
#                 clean[i][1] = str(int(clean[i+1][0]) - 1)
#             elif i == m-1:
#                 clean[i][0] = str(int(clean[i-1][1]) + 1)
#                 clean[i][1] = upper
#             else:
#                 clean[i][0] = str(int(clean[i-1][1]) + 1)
#                 clean[i][1] = str(int(clean[i+1][0]) - 1)

#     return [BIN+y[0]+','+BIN+y[1]+','+y[2] for y in clean]

# input1 = '424242\n4\n0000000000,3700000000,VISA\n1000000000,1299999999,DISCOVER\n4000000000,8999999999,DISCOVER\n6100000000,7999999999,MASTERCARD'
# print(f'input: \n{input1}')
# print(f'output: \n{card_metadata(input1)}') # expected output = ['4242420000000000,4242423999999999,VISA', '4242424000000000,4242429999999999,DISCOVER']

# input2 = '424242\n3\n1000000000,1299999999,VISA\n1000000000,5000000000,AMEX\n6000000000,8000000000,MASTERCARD'
# print(f'input: \n{input2}')
# print(f'output: {card_metadata(input2)}') # expected output = '4242420000000000,4242425999999999,AMEX', '4242426000000000,4242429999999999,MASTERCARD']

# input3 = '424242\n3\n1000000000,5000000000,VISA\n2000000000,3000000000,AMEX\n4000000000,5000000000,MASTERCARD'
# print(f'input: \n{input3}')
# print(f'output: {card_metadata(input3)}') # expected output = '4242420000000000,4242429999999999,VISA']

'''
Part 4: Need to merge intervals
'''
input1 = '424242\n2\n0000000000,5999999999,VISA\n6000000000,9999999999,VISA'
print(f'input: \n{input1}')
print(f'output: \n{card_metadata(input1)}') # expected output = ['4242420000000000,4242429999999999,VISA']

input2 = '424242\n3\n1000000000,3999999999,VISA\n5000000000,6999999999,VISA\n8000000000,9999999999,MASTERCARD'
print(f'input: \n{input2}')
print(f'output: {card_metadata(input2)}') # expected output = '4242420000000000,4242427999999999,VISA', '4242428000000000,4242429999999999,MASTERCARD']