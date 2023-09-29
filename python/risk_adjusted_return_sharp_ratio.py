import pandas as pd
import matplotlib.pyplot as plt
from dataset_cumulative_return import *

# data cleaning - dropping the row with missing value
dsi_us = dsi_us_raw.dropna().copy()
vsgx_global = vsgx_global_raw.dropna().copy()
esge_emerge = esge_emerge_raw.dropna().copy()
iesg_europe = iesg_europe_raw.dropna().copy()
spy_us = spy_us_raw.dropna().copy()
vxus_global = vxus_global_raw.dropna().copy()
vwo_emerge = vwo_emerge_raw.dropna().copy()
vgk_europe = vgk_europe_raw.dropna().copy()

# Setting date as index
dsi_us['Date'] = pd.to_datetime(dsi_us['Date'])
dsi_us.set_index('Date', inplace=True)
vsgx_global['Date'] = pd.to_datetime(vsgx_global['Date'])
vsgx_global.set_index('Date', inplace=True)
esge_emerge['Date'] = pd.to_datetime(esge_emerge['Date'])
esge_emerge.set_index('Date', inplace=True)
iesg_europe['Date'] = pd.to_datetime(iesg_europe['Date'])
iesg_europe.set_index('Date', inplace=True)
spy_us['Date'] = pd.to_datetime(spy_us['Date'])
spy_us.set_index('Date', inplace=True)
vxus_global['Date'] = pd.to_datetime(vxus_global['Date'])
vxus_global.set_index('Date', inplace=True)
vwo_emerge['Date'] = pd.to_datetime(vwo_emerge['Date'])
vwo_emerge.set_index('Date', inplace=True)
vgk_europe['Date'] = pd.to_datetime(vgk_europe['Date'])
vgk_europe.set_index('Date', inplace=True)

# choosing the period of time to display
dsi_us = dsi_us.loc['2018-12':'2023-09']
spy_us = spy_us.loc['2018-12':'2023-09']
vsgx_global = vsgx_global.loc['2018-12':'2023-09']
esge_emerge = esge_emerge.loc['2018-12':'2023-09']
iesg_europe = iesg_europe.loc['2018-12':'2023-09']
vxus_global = vxus_global.loc['2018-12':'2023-09']
vwo_emerge = vwo_emerge.loc['2018-12':'2023-09']
vgk_europe = vgk_europe.loc['2018-12':'2023-09']

# constructing list of etfs
etfs = [dsi_us, spy_us, vsgx_global, esge_emerge, iesg_europe, vxus_global, vwo_emerge, vgk_europe]
names = ['dsi_us', 'spy_us', 'vsgx_global', 'esge_emerge', 'iesg_europe', 'vxus_global', 'vwo_emerge', 'vgk_europe']
colors = ['red', 'blue', 'green', 'brown', 'orange', 'purple', 'pink', 'black']

# Assume constant risk-free rate level
risk_free_rate = 0.025

# Calculate annualized Sharpe ratio for each market
sharpe_ratios = {}
for index, etf in enumerate(etfs):
    mean_daily_return = etf['Daily_Price_return'].mean()
    sd_daily_return = etf['Daily_Price_return'].std()
    annualized_sharpe_ratio = ((mean_daily_return - risk_free_rate / 250) / sd_daily_return) * (252 ** 0.5)
    etf_name = names[index] if names else str(index)
    sharpe_ratios[etf_name] = annualized_sharpe_ratio


# Create a DataFrame for Sharp Ratio
sharpe_df = pd.DataFrame({'ETF': list(sharpe_ratios.keys()), 'Sharpe Ratio': list(sharpe_ratios.values())}).sort_values(
    'Sharpe Ratio', ascending=True)


# Plot the values using a vertical bar chart
plt.figure(figsize=(10, 6))
for index, row in sharpe_df.iterrows():
    plt.bar(row['ETF'], row['Sharpe Ratio'], color=colors[index], label=row['ETF'])
plt.ylabel('Sharpe Ratio')
plt.title('Sharpe Ratios(Risk adjusted return) of all ETFs')
plt.xticks(rotation=45)
num_etfs = len(names)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.98), ncol=num_etfs, title="ETFs", fontsize='small')
plt.tight_layout()
plt.show()

