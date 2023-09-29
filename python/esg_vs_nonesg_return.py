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
dsi_us = dsi_us.loc['2018-10':'2023-09']
spy_us = spy_us.loc['2018-10':'2023-09']
vsgx_global = vsgx_global.loc['2018-10':'2023-09']
esge_emerge = esge_emerge.loc['2018-10':'2023-09']
iesg_europe = iesg_europe.loc['2018-10':'2023-09']
vxus_global = vxus_global.loc['2018-10':'2023-09']
vwo_emerge = vwo_emerge.loc['2018-10':'2023-09']
vgk_europe = vgk_europe.loc['2018-10':'2023-09']

# Calculating cumulative return over time
dsi_us['Cumulative Return'] = (1+dsi_us['Daily_Price_return']).cumprod()
vsgx_global['Cumulative Return'] = (1+vsgx_global['Daily_Price_return']).cumprod()
esge_emerge['Cumulative Return'] = (1+esge_emerge['Daily_Price_return']).cumprod()
iesg_europe['Cumulative Return'] = (1+iesg_europe['Daily_Price_return']).cumprod()
spy_us['Cumulative Return'] = (1+spy_us['Daily_Price_return']).cumprod()
vxus_global['Cumulative Return'] = (1+vxus_global['Daily_Price_return']).cumprod()
vwo_emerge['Cumulative Return'] = (1+vwo_emerge['Daily_Price_return']).cumprod()
vgk_europe['Cumulative Return'] = (1+vgk_europe['Daily_Price_return']).cumprod()

# Combining ESG and Non-ESG ETF
esg_combined = pd.concat([dsi_us['Cumulative Return'], vsgx_global['Cumulative Return'], esge_emerge['Cumulative Return'], iesg_europe['Cumulative Return']], axis=1)
esg_combined['Mean Performance'] = esg_combined.mean(axis=1)
non_esg_combined = pd.concat([spy_us['Cumulative Return'], vxus_global['Cumulative Return'], vwo_emerge['Cumulative Return'], vgk_europe['Cumulative Return']], axis=1)
non_esg_combined['Mean Performance'] = non_esg_combined.mean(axis=1)


# plotting ESG and Non-ESG ETFs return performance over time
plt.figure(figsize=(12,6))
esg_combined['Mean Performance'].plot(label='Mean Performance of all ESG ETFs')
non_esg_combined['Mean Performance'].plot(label='Mean Performance of all Traditional ETFs (Non-ESG)')
# display the final figure on plot
value_esg = esg_combined['Mean Performance'].iloc[-1]
plt.annotate(f"{value_esg:.2f}",
             xy=(esg_combined.index[-1], value_esg),
             xytext=(esg_combined.index[-1], value_esg + 0.08),
             color='blue',
             ha='center')
value_nonesg = non_esg_combined['Mean Performance'].iloc[-1]
plt.annotate(f"{value_nonesg:.2f}",
             xy=(non_esg_combined.index[-1], value_nonesg),
             xytext=(non_esg_combined.index[-1], value_nonesg + 0.03),
             color='orange',
             ha='left')
plt.title('Mean Performance of ESG and Non-ESG ETFs Over Last 5 Years')
plt.ylabel('Mean Cumulative Return')
plt.xlabel('Date')
plt.legend()
plt.grid(True)
plt.show()
