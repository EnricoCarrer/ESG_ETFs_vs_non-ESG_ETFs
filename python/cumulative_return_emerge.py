import pandas as pd
import matplotlib.pyplot as plt
from dataset_cumulative_return import *


# data cleaning - dropping the row with missing value
esge_emerge = esge_emerge_raw.dropna().copy()
vwo_emerge = vwo_emerge_raw.dropna().copy()

# Setting date as index
esge_emerge['Date'] = pd.to_datetime(esge_emerge['Date'])
esge_emerge.set_index('Date', inplace=True)

vwo_emerge['Date'] = pd.to_datetime(vwo_emerge['Date'])
vwo_emerge.set_index('Date', inplace=True)

# choosing the period of time to display
esge_emerge = esge_emerge.loc['2016-08':'2023-09']
vwo_emerge = vwo_emerge.loc['2016-08':'2023-09']

# Calculating cumulative return over time
esge_emerge['Cumulative Return'] = (1+esge_emerge['Daily_Price_return']).cumprod()
vwo_emerge['Cumulative Return'] = (1+vwo_emerge['Daily_Price_return']).cumprod()

# Returning the final outcome of cumulative returns
esge_last_return = round(esge_emerge['Cumulative Return'].iloc[-1], 2)
vwo_last_return = round(vwo_emerge['Cumulative Return'].iloc[-1], 2)
print('The cumulative return of ESG is:')
print(esge_last_return)
print('')
print('The cumulative return of Non-ESG is:')
print(vwo_last_return)
print('')
if esge_last_return > vwo_last_return:
    print('ESG ETF performance is better in Emerging market in long run.')
else:
    print('ESG ETF is under-performing the traditional ETF in Emerging market.')

# Returning visualisation Plot
plt.figure()
plt.plot(esge_emerge['Cumulative Return'], label='ESGE_Emerge')
plt.plot(vwo_emerge['Cumulative Return'], label='VWO_Emerge')
plt.legend()
plt.title('Comparison of ESG and NON-ESG Cumulative Returns in Emerging Market')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.show()
