import oandapyV20
import oandapyV20.endpoints.transactions as trans
import csv
from pprint import pprint
accessToken = 'c5aa24460adc142a87e4b1bd339376ed-47f0e6c248fec1c7cdcb8b61fd481330'
accountID = '101-011-16913927-001'
client = oandapyV20.API(access_token=accessToken)
params ={"to": 300,"from": 200}
r = trans.TransactionIDRange(accountID=accountID, params=params)
client.request(r)
result = r.response['transactions']
# pprint(result)
# print('{} {} {} units :{} {} price :{}'.format(result[6]['id'],result[6]['time'],result[6]['instrument'],result[6]['units'],result[6]['type'],result[6]['price']))

for i in range(len(result)):

    
    # print('รอบที่ {}'.format(i))
    if result[i]['type'] == 'DAILY_FINANCING'or result[i]['type'] == 'ORDER_CANCEL':
        with open('total.csv','a',newline='')as f:
            fw = csv.writer(f)
            fw.writerow(['{} {} {}'.format(result[i]['id'],result[i]['time'],result[i]['type'])])
        

    elif result[i]['type'] == 'LIMIT_ORDER':
        with open('total.csv','a',newline='') as f:
            fw = csv.writer(f)
            fw.writerow(['{} {} {} units :{} {} price :{}'.format(result[i]['id'],result[i]['time'],result[i]['instrument'],result[i]['units'],result[i]['type'],result[i]['price'])])
def demo2():
    with open('total.csv','w',newline='') as f:
        one = 1
        two = 2
        fw = csv.writer(f)
        fw.writerow(['{} {}'.format(one,two)])

