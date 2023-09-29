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

# Calculating Standard Deviation and store in list
list_sd = []
for etf in etfs:
    sd = etf['Daily_Price_return'].std()
    list_sd.append(sd)

list_sd_df = pd.DataFrame({'ETF': names, 'Standard Deviation': list_sd}).sort_values('Standard Deviation', ascending=True)

# plotting the S.D. as bar chart for comparison
plt.figure(figsize=(10, 6))
for index, row in list_sd_df.iterrows():
    plt.bar(row['ETF'], row['Standard Deviation'], color=colors[index], label=row['ETF'])
# plt.bar(list_sd_df['ETF'], list_sd_df['Standard Deviation'], color=colors)
plt.ylabel('Standard Deviation')
plt.title('Risk Measure (Standard Deviation) of all ETFs')
plt.xticks(rotation=45)
upper_limit = 1.25 * list_sd_df['Standard Deviation'].max()
plt.ylim(0, upper_limit)
counts_etfs = len(names)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.98), ncol=counts_etfs, title="ETFs", fontsize="small")
plt.tight_layout()
plt.show()



