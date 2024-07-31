import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV file
file_path = 'PNL_calculating/test_logs.csv'
data = pd.read_csv(file_path, delimiter=';')

# Convert currentTime from nanoseconds to a readable datetime format
data['currentTime'] = pd.to_datetime(data['currentTime'], unit='ns')

# Filter out only the filled orders to calculate PnL
filled_orders = data[data['action'] == 'filled']

# Calculate the gross PnL for each trade
filled_orders['PnL'] = filled_orders['tradePx'] * filled_orders['tradeAmt']
filled_orders.loc[filled_orders['orderSide'] == 'sell', 'PnL'] *= -1

# 1. Calculate total gross PnL
total_gross_pnl = filled_orders['PnL'].sum()
print(f"Total Gross PnL: {total_gross_pnl}")

# 2. Calculate total gross PnL over each security ID
pnl_per_security = filled_orders.groupby('orderProduct')['PnL'].sum()
print("Total Gross PnL per Security ID:")
print(pnl_per_security)

# 3. Draw cumulative gross PnL
filled_orders['cumulative_PnL'] = filled_orders['PnL'].cumsum()

# Plot cumulative gross PnL over time
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(filled_orders['currentTime'], filled_orders['cumulative_PnL'], label='Cumulative PnL')
plt.xlabel('Time')
plt.ylabel('Cumulative Gross PnL')
plt.title('Cumulative Gross PnL over Time')
plt.legend()
plt.grid(True)

# Add total gross PnL annotation
plt.text(0.95, 0.01, f'Total Gross PnL: {total_gross_pnl:.2f}', verticalalignment='bottom', horizontalalignment='right', transform=plt.gca().transAxes, color='green', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

# Plot total gross PnL per security ID
plt.subplot(2, 1, 2)
pnl_per_security.plot(kind='bar')
plt.xlabel('Security ID')
plt.ylabel('Total Gross PnL')
plt.title('Total Gross PnL per Security ID')
plt.grid(True)

# Annotate the bar plot with PnL values
for index, value in enumerate(pnl_per_security):
    plt.text(index, value, f'{value:.2f}', ha='center', va='bottom')

# Show the plots
plt.tight_layout()
plt.show()