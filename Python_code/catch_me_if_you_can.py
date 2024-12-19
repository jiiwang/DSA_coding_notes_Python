input1 = ['approved', 'invalid_pin', 'expired_card']
input2 = ['do_not_honor', 'stolen_card', 'lost_card']
input3 = 'retail,5 \n airline,2 \n restaurant,10 \n venue,3'
input4 = 'acct_1,airline \n acct_2,venue \n acct_3,retail'
input5 = 0
input6 = 'CHARGE,ch_1,acct_1,100,do_not_honor \n \
          CHARGE,ch_2,acct_1,200,approved \n \
          CHARGE,ch_3,acct_1,300,do_not_honor \n \
          CHARGE,ch_4,acct_2,100,lost_card \n \
          CHARGE,ch_5,acct_2,200,lost_card \n \
          CHARGE,ch_6,acct_2,300,lost_card \n \
          CHARGE,ch_7,acct_3,100,lost_card \n \
          CHARGE,ch_8,acct_2,200,stolen_card \n \
          CHARGE,ch_9,acct_3,100,approved'

# expected output = 'acct_1,acct_2'