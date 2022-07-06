accounts = [
    {
        "acno": 1000, "ac_type": "savings", "balance": 5000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1001, "ac_type": "savings", "balance": 6000, "transactions": [
        {"to": 1000, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1002, "ac_type": "current", "balance": 8000, "transactions": [
        {"to": 1001, "amount": 700, "note": "ebill", "method": "g-pay"},
        {"to": 1000, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 800, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1003, "ac_type": "credit", "balance": 15000, "transactions": [
        {"to": 1001, "amount": 1500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 800, "note": "geto", "method": "neft"},
        {"to": 1000, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1004, "ac_type": "savings", "balance": 50000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },

]

#q1  print details of 1002

#for ac in accounts:
 #   if ac["acno"]==1002:
  #      transactions=ac.pop("transactions")  #given transactione remoove akkunnu pop
   #     print(ac)

ac_details=[ ac for ac in accounts if ac["acno"]==1002]
#print(ac_details)

#Q2 print savings type account details:

save_type=[ac for ac in accounts if ac["ac_type"]=="savings"]
#print(save_type)

#Q3 sort acount based on balence order by desc  (#ithe oru list ane athe konde ane sort cheyyan e method)

#accounts.sort(reverse=True,key=lambda ac:ac["balance"])
#print(accounts)

#Q4 print all phonepay transactions

  #transactions matharam eduthu

#all_transaction=[ac["transactions"]for ac in accounts]
#phone_pay=[ trans for tlist in all_transaction for trans in tlist if trans["method"]=="phone-pay"] #athine flattern list akki athil ninne phone pay eduthe
#print(phone_pay)

#Q4  print tansactions when amount>500
all_transaction=[ac["transactions"]for ac in accounts]
stamount5=[trans for tlist in all_transaction for trans in tlist if trans["amount"]>500]
print(stamount5)

#Q5 credit transactions of 1002
#credit_trans=[trans for tlist in all_transaction for trans in tlist]






#Q6 Aggregate transactions based on paymentmode

pms={}
all_transaction=[ac["transactions"]for ac in accounts] #transactions mathram eduthu
transactions=[t for tlist in all_transaction for t in tlist] #flattern lis akki

for transaction in transactions:
    p_method=transaction["method"]
    amount=transaction["amount"]
    if p_method in pms:
        pms[p_method]+=amount
    else:
        pms[p_method]=amount
print(pms)
