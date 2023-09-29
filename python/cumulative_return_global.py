import pandas as pd
import matplotlib.pyplot as plt
from dataset_cumulative_return import *

# data cleaning - dropping the row with missing value
vsgx_global = vsgx_global_raw.dropna().copy()
vxus_global = vxus_global_raw.dropna().copy()

# Setting date as index
vsgx_global['Date'] = pd.to_datetime(vsgx_global['Date'])
vsgx_global.set_index('Date', inplace=True)

vxus_global['Date'] = pd.to_datetime(vxus_global['Date'])
vxus_global.set_index('Date', inplace=True)

# choosing the period of time to display
vsgx_global = vsgx_global.loc['2018-10':'2023-09']
vxus_global = vxus_global.loc['2018-10':'2023-09']

# Calculating cumulative return over time
vsgx_global['Cumulative Return'] = (1+vsgx_global['Daily_Price_return']).cumprod()
vxus_global['Cumulative Return'] = (1+vxus_global['Daily_Price_return']).cumprod()

# Returning the final outcome of cumulative returns
vsgx_last_return = round(vsgx_global['Cumulative Return'].iloc[-1], 2)
vxus_last_return = round(vxus_global['Cumulative Return'].iloc[-1], 2)
print('The cumulative return of ESG is:')
print(vsgx_last_return)
print('')
print('The cumulative return of Non-ESG is:')
print(vxus_last_return)
print('')
if vsgx_last_return > vxus_last_return:
    print('ESG ETF performance is better in Global market in long run.')
else:
    print('ESG ETF is under-performing the traditional ETF in Global market.')

# Returning visualisation Plot
plt.figure()
plt.plot(vsgx_global['Cumulative Return'], label='VSGX_Global')
plt.plot(vxus_global['Cumulative Return'], label='VXUS_Global')
plt.legend()
plt.title('Comparison of ESG and NON-ESG Cumulative Returns in Global market(Ex-US)')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.show()
