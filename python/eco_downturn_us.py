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

# choosing the period of time to display
spy_us = spy_us.loc['2007-02':'2009-12']
dsi_us = dsi_us.loc['2007-02':'2009-12']

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
    print('ESG ETF performance is better in US market in economic downturn.')
else:
    print('ESG ETF is under-performing the traditional ETF in US market in downturn.')

# Returning visualisation Plot
plt.figure()
plt.plot(spy_us['Cumulative Return'], label='SPY_US')
plt.plot(dsi_us['Cumulative Return'], label='DSI_US')
# display the final figure on plot
value_spy = spy_us['Cumulative Return'].iloc[-1]
plt.annotate(f"{value_spy:.2f}",
             xy=(spy_us.index[-1], value_spy),
             xytext=(spy_us.index[-1], value_spy + -0.05),
             color='blue',
             ha='center')
value_dsi = dsi_us['Cumulative Return'].iloc[-1]
plt.annotate(f"{value_dsi:.2f}",
             xy=(dsi_us.index[-1], value_dsi),
             xytext=(dsi_us.index[-1], value_dsi + 0.02),
             color='orange',
             ha='center')
plt.legend()
plt.title('Comparison of ESG and NON-ESG Returns in US market during recession (2007-2009)')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.grid(True)
plt.show()
