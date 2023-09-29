import pandas as pd
import matplotlib.pyplot as plt
from dataset_cumulative_return import *

# data cleaning - dropping the row with missing value
iesg_europe = iesg_europe_raw.dropna().copy()
vgk_europe = vgk_europe_raw.dropna().copy()

# Setting date as index
iesg_europe['Date'] = pd.to_datetime(iesg_europe['Date'])
iesg_europe.set_index('Date', inplace=True)

vgk_europe['Date'] = pd.to_datetime(vgk_europe['Date'])
vgk_europe.set_index('Date', inplace=True)

# choosing the period of time to display
iesg_europe = iesg_europe.loc['2011-03':'2023-09']
vgk_europe = vgk_europe.loc['2011-03':'2023-09']

# Calculating cumulative return over time
iesg_europe['Cumulative Return'] = (1+iesg_europe['Daily_Price_return']).cumprod()
vgk_europe['Cumulative Return'] = (1+vgk_europe['Daily_Price_return']).cumprod()

# Returning the final outcome of cumulative returns
iesg_last_return = round(iesg_europe['Cumulative Return'].iloc[-1], 2)
vgk_last_return = round(vgk_europe['Cumulative Return'].iloc[-1], 2)
print('The cumulative return of ESG is:')
print(iesg_last_return)
print('')
print('The cumulative return of Non-ESG is:')
print(vgk_last_return)
print('')
if iesg_last_return > vgk_last_return:
    print('ESG ETF performance is better in Europe market in long run.')
else:
    print('ESG ETF is under-performing the traditional ETF in Europe market.')

# Returning visualisation Plot
plt.figure()
plt.plot(iesg_europe['Cumulative Return'], label='IESGE_Europe')
plt.plot(vgk_europe['Cumulative Return'], label='VGK_Europe')
plt.legend()
plt.title('Comparison of ESG and NON-ESG Cumulative Returns in Europe Market')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.show()
