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

# Calculating cumulative return over time
dsi_us['Cumulative Return'] = (1+dsi_us['Daily_Price_return']).cumprod()
vsgx_global['Cumulative Return'] = (1+vsgx_global['Daily_Price_return']).cumprod()
esge_emerge['Cumulative Return'] = (1+esge_emerge['Daily_Price_return']).cumprod()
iesg_europe['Cumulative Return'] = (1+iesg_europe['Daily_Price_return']).cumprod()
spy_us['Cumulative Return'] = (1+spy_us['Daily_Price_return']).cumprod()
vxus_global['Cumulative Return'] = (1+vxus_global['Daily_Price_return']).cumprod()
vwo_emerge['Cumulative Return'] = (1+vwo_emerge['Daily_Price_return']).cumprod()
vgk_europe['Cumulative Return'] = (1+vgk_europe['Daily_Price_return']).cumprod()

# Calculating excess return for each market
dsi_us['Excess Return'] = dsi_us['Cumulative Return'] - spy_us['Cumulative Return']
vsgx_global['Excess Return'] = vsgx_global['Cumulative Return'] - vxus_global['Cumulative Return']
esge_emerge['Excess Return'] = esge_emerge['Cumulative Return'] - vwo_emerge['Cumulative Return']
iesg_europe['Excess Return'] = iesg_europe['Cumulative Return'] - vgk_europe['Cumulative Return']

# Plotting the excess return and red highlighting the negative performance
plt.figure(figsize=(12, 6))
dsi_us['Excess Return'].plot(label='Excess return of US market ESG ETF', color='red')
vsgx_global['Excess Return'].plot(label='Excess return of Global(Ex US) market ESG ETF', color='blue')
esge_emerge['Excess Return'].plot(label='Excess return of Emerging market ESG ETF', color='green')
iesg_europe['Excess Return'].plot(label='Excess return of Europe market ESG ETF', color='orange')
plt.title('Excess Return of ESG ETFs in all markets Over Last 5 Years')
plt.ylabel('Excess Return')
plt.xlabel('Date')
plt.grid(True)
ax = plt.gca()
ax.axhspan(ymin=ax.get_ylim()[0], ymax=0, facecolor='red', alpha=0.2)
plt.legend()
plt.show()



