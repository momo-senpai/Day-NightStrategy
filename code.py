#importing required modules
import pandas as pd
import yfinance as yf
import datetime 

# Taking investment amount and Date of Investment as input
Investment = int(input('Enter Investment Amount in $ '))
sd = input('Enter Date of Investment in DD-MM-YYYY format: ').split('-')
start_date = datetime.date(int(sd[2]), int(sd[1]), int(sd[0]))
end_date = datetime.datetime.today()

# using yahoo finance api to access stock data for inputted time period
amzn_data = yf.download('AMZN', start= start_date, end= end_date)
aapl_data = yf.download('AAPL', start= start_date, end= end_date)

# reseting index for easier access of Date
amzn = pd.DataFrame(amzn_data)
amzn.reset_index(inplace=True)
aapl = pd.DataFrame(aapl_data)
aapl.reset_index(inplace=True)


#cleaning the data
amzn.drop(['High','Low','Adj Close', 'Volume'],axis=1,inplace=True)
aapl.drop(['High','Low','Adj Close', 'Volume'],axis=1,inplace=True)

# Calculating overnight return % by using ((Open-Prev.CLose)/Close)*100 for AMZN
amzn['Overnight Return %'] = ((amzn['Open'].shift(-1) - amzn['Close']).shift(1)/amzn['Close'])*100
amzn['Overnight Return %'] = amzn['Overnight Return %'].fillna(0)

# Calculating overnight return % by using ((Open-Prev.CLose)/Close)*100 for AAPL
aapl['Overnight Return %'] = ((aapl['Open'].shift(-1) - aapl['Close']).shift(1)/aapl['Close'])*100 
aapl['Overnight Return %'] = aapl['Overnight Return %'].fillna(0)


#Printing Daily overnight returns and total Profit & Loss(AMZN)
print(str(Investment)+'$ invested in Amazon Stock on',start_date) 
amzn_investment = Investment
amzn_profit = 0
for i in range(1,amzn['Date'].count()):
    amzn_pnl =  (amzn['Overnight Return %'][i]/100)*Investment
    print('PnL on',amzn['Date'][i],'is $',amzn_pnl)
    amzn_profit = amzn_profit + amzn_pnl
print('Current Investment Value: ',(amzn_investment+amzn_profit))
print('Total PnL % :',((amzn_profit/Investment)*100).round(3))

 #Printing Daily overnight returns and total Profit & Loss(AMZN)
print(str(Investment)+'$ invested in Apple Stock on',start_date) 
aapl_investment = Investment
aapl_profit = 0
for i in range(1,aapl['Date'].count()):
    aapl_pnl =  (aapl['Overnight Return %'][i]/100)*Investment
    print('PnL on',aapl['Date'][i],'is',aapl_pnl)
    aapl_profit = aapl_profit + aapl_pnl
print('Current Investment Value',(aapl_investment+aapl_profit))
print('Total PnL % :',((aapl_profit/Investment)*100).round(3))

