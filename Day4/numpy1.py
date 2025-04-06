import numpy as np
import pandas as pd
from random import randint

np.random.randint(30)

stock_prices = np.random.uniform(100, 500, size=(30, 5))
df = pd.DataFrame(stock_prices, columns=["Company_A", "Company_B", "Company_C", "Company_D", "Company_E"])
print(df)

average_prices = stock_prices.mean(axis=0)
print(f"Average stock prices: {average_prices}")

max_price = stock_prices.max()
day, company = divmod(stock_prices.argmax(), stock_prices.shape[1])
print(f"Highest price recorded: {max_price:.2f} at Day {day + 1}, Company {company + 1}")


normalized = (stock_prices - stock_prices.min()) / (stock_prices.max() - stock_prices.min())
df = pd.DataFrame(normalized, columns=["Company_A", "Company_B", "Company_C", "Company_D", "Company_E"])
print(df)


risky_days = np.where(stock_prices <= 199)
unique_risky_days = np.unique(risky_days[0])
print("\nRisky Investment Days:")

for day in unique_risky_days:
    risky_values = stock_prices[day, stock_prices[day] < 200]
    print(f"Day {day + 1}: {risky_values}")


#p = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$"
