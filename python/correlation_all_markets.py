import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

# Storing ETFs and benchmarks in a dictionary
list_esg = {
    'DSI US': dsi_us,
    'VSGX Global': vsgx_global,
    'ESGE Emerge': esge_emerge,
    'IESG Europe': iesg_europe
}

list_benchmark = {
    'DSI US': spy_us,
    'VSGX Global': vxus_global,
    'ESGE Emerge': vwo_emerge,
    'IESG Europe': vgk_europe
}

# Calculating correlations between each ETF and its benchmark
correlation_values = {}
for name in list_esg:
    correlation_values[name] = list_esg[name]['Daily_Price_return'].corr(list_benchmark[name]['Daily_Price_return'])

correlations = pd.Series(correlation_values)
correlations_clean = correlations.to_frame().T

# visualising with heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlations_clean, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt=".3f")
plt.title('Correlation Heatmap between ETFs and their Benchmarks')
plt.show()


