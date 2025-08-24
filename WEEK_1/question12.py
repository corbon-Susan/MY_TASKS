# 12. Simulated USSD Menu Interaction
#  - You are to design a mock USSD interface for a mobile service.
#  - Requirements:
#    1. When the user runs the program, display a welcome screen with a Nigerian context greeting.
#    2. Ask the user to "dial" a USSD code (e.g., *123#) and store it in a variable.
#    3. Print a menu with at least 3 options (e.g., "Check Balance", "Buy Airtime", "Buy Data") using newline escape sequences `(\n)` for formatting.
#    4. Ask the user to choose an option (1, 2, or 3) and store their choice in a variable.
#    5. Use f-strings and/or concatenation to display a confirmation message showing the selected option.
#    6. Ask for an amount (if applicable) and store it as a number using type casting.
#    7. Display a final message summarizing the transaction.


print(" Hello, Welcome to LIZZY mobile banking service,\n dial *121# to start")
ussd_code = input("Press USSD Code  ")
balance=7000
while True:
    if ussd_code!="*121#":
     print("wrong USSD!")
    else:
        user_option = int(input("choose your option:\n1= check balance\n2=Transfer\n3= withdrawal  "))
    if user_option ==1:
        print(" check balance")
    if user_option == 2:
        print("Tranfer")
    if user_option == 3:
        print("withdrawal")
    if user_option != 1 and 2 and 3:
           print("Enter a valid option")
    print(f"your current balance is \u20A6 {balance:,}")
    Amount=  int(input("enter the amount you want to withdrawal or transfer  "))
    balance1 = balance - Amount
    print(f"your withdrawal :{Amount:,} \n new balance :\u20A6 {balance1:,}\n Thank you for using our service!")
    break

