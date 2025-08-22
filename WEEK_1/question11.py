
# Nigerian Currency Converter (Very Advanced)
#   - Ask for:
#     - Amount in Naira (float)
#     - Exchange rate to US Dollars (float)
#     - Exchange rate to British Pounds (float)
# - Convert and print results with thousands separators and currency symbols, neatly aligned in a table-like format using escape sequences.


Amount_Naira = float(input(" Enter the amount you have   \u20A6 "))
US_Dollar_rate = float(input(" Dollar excahnge rate"))
British_pound_rate = float(input( " Exchange rate"))
converted_Amount_USD= Amount_Naira/US_Dollar_rate 
converted_Amount_pound =Amount_Naira /British_pound_rate
print(f"your converted amount in US dollar:${converted_Amount_USD}\n your converted amount in British Pound: \u20A4{converted_Amount_pound}")


