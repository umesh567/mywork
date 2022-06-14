account = {"acc_no": 1000,
           "open_date": "34-08-5678",
                        "type":"save",
                               "p_name": "ram",}

print(account["acc_no"])


print ("balence" in account)

account["balence"]="5000"
print(account)

account["balence"]+=1000
print(account)