# 1. Read csv from google and load to dataframe pandas
# 2. Select column DateId, eutrancellfdd, cbra
# array 1d, 2d ==> series (kol), dataframe (kol x bar)
import pandas as pd

# Replace 'FILE_ID' with the actual file ID from the shareable link
# file_id = '12L0VFSB4VR3JEa01loe4T3niOHpWuL4kdVpvVGAgcik'

# Construct the download link
# download_link = f"https://docs.google.com/spreadsheets/d/{file_id}/edit#gid=0"
download_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTKWlYVX6hQTvXMqmvXRQBOOTsgjrzgBtcGJkf8Kdvb6pVb2urUMfgkoWoVw6KnSUh9apFETf_n9gqm/pub?output=csv"

# df = pd.read_csv(download_link)
df = pd.read_csv(download_link, usecols=['DateId', 'EUtranCellFDD','LTE_CBRA_SR','LTE_TxRank2'])
print(df.dtypes)
import sys

# 3. Filter specific DateId (7 days)
df['DateId'] = pd.to_datetime(df['DateId'])
# start_date = pd.to_datetime('2023-09-20')
start_date = sys.argv[1]
end_date = sys.argv[2]
# end_date = pd.to_datetime('2023-09-30')
df_output = df[(df['DateId'] >= start_date) & (df['DateId'] <= end_date)]

# filtered_df = df[(df['DateId'] >= start_date) & (df['DateId'] <= pd.to_datetime('2023-09-30'))]
# filtered_df = df[(df['DateId'] >= start_date) ]
print(df_output)

# 4. Generate line chart, using matplotlib
import matplotlib.pyplot as plt

# Create a Matplotlib figure and axis
fig, ax = plt.subplots()

# Plot the first line series from df1
ax.plot(df_output['DateId'], df_output['LTE_CBRA_SR'], label='LTE_CBRA_SR')

# Plot the second line series from df2
ax.plot(df_output['DateId'], df_output['LTE_TxRank2'], label='LTE_TxRank2')

# Add labels, title, and legend
ax.set_xlabel('Date')
ax.set_ylabel('%')
ax.set_title('CBRA vs TxRank2')
ax.legend()

# Display the plot
plt.show()