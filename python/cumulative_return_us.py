import pandas as pd
import matplotlib.pyplot as plt
from dataset_cumulative_return import *

# data cleaning - dropping the row with missing value
spy_us = spy_us_raw.dropna().copy()
dsi_us = dsi_us_raw.dropna().copy()

# Setting date as index
spy_us['Date'] = pd.to_datetime(spy_us['Date'])
spy_us.set_index('Date', inplace=True)

dsi_us['Date'] = pd.to_datetime(dsi_us['Date'])
dsi_us.set_index('Date', inplace=True)

# Calculating cumulative return over time
spy_us['Cumulative Return'] = (1+spy_us['Daily_Price_return']).cumprod()
dsi_us['Cumulative Return'] = (1+dsi_us['Daily_Price_return']).cumprod()

# Returning the final outcome of cumulative returns
dsi_last_return = round(dsi_us['Cumulative Return'].iloc[-1], 2)
spy_last_return = round(spy_us['Cumulative Return'].iloc[-1], 2)
print('The cumulative return of ESG is:')
print(dsi_last_return)
print('')
print('The cumulative return of Non-ESG is:')
print(spy_last_return)
print('')
if dsi_last_return > spy_last_return:
    print('ESG ETF performance is better in US market in long run.')
else:
    print('ESG ETF is under-performing the traditional ETF in US market.')

# Returning visualisation Plot
plt.figure()
plt.plot(spy_us['Cumulative Return'], label='SPY_US')
plt.plot(dsi_us['Cumulative Return'], label='DSI_US')
plt.legend()
plt.title('Comparison of ESG and NON-ESG Cumulative Returns in US market')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.show()
