# Daily Market Report( Ask the user to input market name, number of traders, daily revenue in Naira, Display the result using formatting with commas for thousand separators)

Market_name = input("enter a market you know")
Num_traders = int(input("\u20A6:enter the number of traders"))
Daily_rev = int(input("enter the amount you make daily"))
print(f"{Market_name} Market  has {Num_traders}  traders and their daily revenue is {Daily_rev :,} naira")
