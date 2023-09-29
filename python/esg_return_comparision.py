from dataset_cumulative_return import *

# data cleaning - dropping the row with missing value
dsi_us = dsi_us_raw.dropna().copy()
vsgx_global = vsgx_global_raw.dropna().copy()
esge_emerge = esge_emerge_raw.dropna().copy()
iesg_europe = iesg_europe_raw.dropna().copy()

# Setting date as index
dsi_us['Date'] = pd.to_datetime(dsi_us['Date'])
dsi_us.set_index('Date', inplace=True)
vsgx_global['Date'] = pd.to_datetime(vsgx_global['Date'])
vsgx_global.set_index('Date', inplace=True)
esge_emerge['Date'] = pd.to_datetime(esge_emerge['Date'])
esge_emerge.set_index('Date', inplace=True)
iesg_europe['Date'] = pd.to_datetime(iesg_europe['Date'])
iesg_europe.set_index('Date', inplace=True)

# choosing the period of time to display
dsi_us = dsi_us.loc['2018-10':'2023-09']
vsgx_global = vsgx_global.loc['2018-10':'2023-09']
esge_emerge = esge_emerge.loc['2018-10':'2023-09']
iesg_europe = iesg_europe.loc['2018-10':'2023-09']

# Calculating cumulative return over time
dsi_us['Cumulative Return'] = (1+dsi_us['Daily_Price_return']).cumprod()
vsgx_global['Cumulative Return'] = (1+vsgx_global['Daily_Price_return']).cumprod()
esge_emerge['Cumulative Return'] = (1+esge_emerge['Daily_Price_return']).cumprod()
iesg_europe['Cumulative Return'] = (1+iesg_europe['Daily_Price_return']).cumprod()


# returning the esg all markets visualisation plotting
plt.figure()
plt.plot(vsgx_global['Cumulative Return'], label='VSGX_Global')
plt.plot(dsi_us['Cumulative Return'], label='DSI_US')
plt.plot(esge_emerge['Cumulative Return'], label='ESGE_Emerge')
plt.plot(iesg_europe['Cumulative Return'], label='IESG_Europe')
plt.legend()
plt.title('Comparison of ESG ETF across different markets(5-years)')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.show()

