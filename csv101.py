import time
import oandapyV20
import oandapyV20.endpoints.transactions as trans
import csv
import json

from oandapyV20 import API
import oandapyV20.endpoints.orders as orders
from oandapyV20.contrib.requests import LimitOrderRequest
import oandapyV20
import oandapyV20.endpoints.positions as positions
import oandapyV20.endpoints.pricing as pricing
import oandapyV20.endpoints.transactions as trans
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.orders as orders
from oandapyV20.contrib.requests import MarketOrderRequest
from oandapyV20.contrib.requests import LimitOrderRequest
from oandapyV20.contrib.requests import TradeCloseRequest
from oandapyV20.contrib.requests import PositionCloseRequest
from oandapyV20.contrib.requests import TakeProfitOrderRequest
import oandapyV20.endpoints.trades as trades
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


def getTime():
  named_tuple = time.localtime() # get struct_time
  Time = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
  print(Time)
  print('GRID TRADING ', 'OANDA')

def get_Price():
    client = oandapyV20.API(access_token=accessToken)
    params = {'instruments' : 'XAU_USD'}
    r = pricing.PricingInfo(accountID,params = params)
    client.request(r)
    result = r.response
    result = float(result['prices'][0]['closeoutBid'])
    #print('XAU_USD = ',result,'$')
    # print(' ')
    return result

def get_Balance():
    client = oandapyV20.API(access_token=accessToken)
    r = accounts.AccountDetails(accountID)
    client.request(r)
    result = r.response
    print('Balance :',result['account']['balance'])
    print('NAV :',result['account']['NAV'])
    print('unrealizedpl :',result['account']['positions'][0]['unrealizedPL'])

def orderList():
    client = oandapyV20.API(access_token= accessToken)
    r = orders.OrderList(accountID)
    client.request(r)
    print(r.response)

def demo1():
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

orderList()