import oandapyV20
import oandapyV20.endpoints.transactions as trans
from pprint import pprint
accessToken = 'c5aa24460adc142a87e4b1bd339376ed-47f0e6c248fec1c7cdcb8b61fd481330'
accountID = '101-011-16913927-001'
client = oandapyV20.API(access_token=accessToken)
params ={"to": 207,"from": 200}
r = trans.TransactionIDRange(accountID=accountID, params=params)
client.request(r)
result = r.response['transactions']
pprint(result[6])
print('{} {} {} units :{} {} price :{}'.format(result[6]['id'],result[6]['time'],result[6]['instrument'],result[6]['units'],result[6]['type'],result[6]['price']))
for i in range(len(result)):
    # print('รอบที่ {}'.format(i))
    if result[i]['type'] == 'DAILY_FINANCING'or result[i]['type'] == 'ORDER_CANCEL':
        # print('{} {} {}'.format(result[i]['id'],result[i]['time'],result[i]['type']))
        pass
    # elif result[i]['type'] == 'LIMIT_ORDER':
        # print('{} {} {} {}'.format(result[i]['id'],result[i]['time'],result[i]['instrument'],result[i]['price']))


