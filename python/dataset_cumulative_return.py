import pandas as pd
import matplotlib.pyplot as plt

# converting from Excel file and storing in dataframe
combined_etf = pd.ExcelFile('etf_combined_with_returns.xlsx')

# converting each worksheet and storing in dataframe
spy_us_raw = pd.read_excel('etf_combined_with_returns.xlsx', sheet_name='SPY_US')
dsi_us_raw = pd.read_excel('etf_combined_with_returns.xlsx', sheet_name='DSI_US')
vsgx_global_raw = pd.read_excel('etf_combined_with_returns.xlsx', sheet_name='VSGX_Global')
vxus_global_raw = pd.read_excel('etf_combined_with_returns.xlsx', sheet_name='VXUS_Global')
esge_emerge_raw = pd.read_excel('etf_combined_with_returns.xlsx', sheet_name='ESGE_Emerge')
vwo_emerge_raw = pd.read_excel('etf_combined_with_returns.xlsx', sheet_name='VWO_Emerge')
iesg_europe_raw = pd.read_excel('etf_combined_with_returns.xlsx', sheet_name='IESG_Europe')
vgk_europe_raw = pd.read_excel('etf_combined_with_returns.xlsx', sheet_name='VGK_Europe')



# data cleaning - checking how many of the null value on each column
# print(spy_us_raw.info())
# print(dsi_us_raw.info())
# print(vsgx_global_raw.info())
# print(vxus_global_raw.info())
# print(esgx_emerge_raw.info())
# print(vwo_emerge_raw.info())
# print(iesg_europe_raw.info())
# print(vgk_europe_raw.info())



