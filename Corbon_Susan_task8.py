# **Task1**
# - Explain each output of the program below.
# - Give 3 usecases or cenarios where you can apply the program below.
# - Write the code for 1 of the 3 use cases.


 num1 = int(input("Enter first number: "))
 num2 = int(input("Enter second number"))
print(f"{num1} == {num2} : {num1 == num2}")     # The output might be true or false depending on the values the user input(== equal to) num 1 must be equal in value to num2.
print(f"{num1} != {num2} : {num1 != num2}")  # True if the num1 is not equal to num2 in value
print(f"{num1} > {num2} : {num1 > num2}")  # it can either be true or false (the num1 must be bigger in value than num2 =true, num1 smaller in value than num2 = False)
print(f"{num1} < {num2} : {num1 < num2}") # ti can either be true or false (the num1 must be smaller in value than num2 =true, num1 bigger in value than num2 = False)


#use case
# 1. it can be used to compare the accademic performance of a student in different terms
# 2. To check the prices of goods on monthly basis
# 3. To comapre the school fees paid


#Use case - (MONTHLY COMMMODITY PRICE CHECKER)
 June_cost_of_goods =  int(input(" What is the cost of indomie last month?"))
 July_cost_0f_goods = int(input("what is the current cost of indomie?"))

print(f"{June_cost_of_goods} >= {July_cost_0f_goods}:{July_cost_0f_goods >= June_cost_of_goods}")
print(f"{June_cost_of_goods}== {July_cost_0f_goods}:{June_cost_of_goods == July_cost_0f_goods}")
print(f"{June_cost_of_goods}=! {July_cost_0f_goods}:{June_cost_of_goods != July_cost_0f_goods}")
print(f"{June_cost_of_goods}<= {July_cost_0f_goods}:{June_cost_of_goods <= July_cost_0f_goods}")

July_cost_0f_goods -= June_cost_of_goods
print("Cost difference:", July_cost_0f_goods)


#**Task2**
# - Comment the code below appropriately, and using doctring, explain what the code is doing.
# -  Adapt the code to the case below.

# - Federal Government Scholarship Key Eligibility Requirements:
#   - Citizenship:
#     - Applicant must be a citizen of Nigeria. 
#   - Enrollment:
#     - Must be a registered, full-time undergraduate student in a recognized Nigerian university. 
#   - Other Scholarships:
#     - Applicants cannot be currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international. 
#   - Academic Qualification:
#     - For undergraduate courses, applicants usually need five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics.

# name= input("Emter your name :")        #collect user's name
# age= int(input("Enter your age :"))     # collects user's age
# Score = int(input("emter your test score:"))  #collects user'sscore
# eligibility = (age < 18) and (Score >70)    # check for elligibilty using the "And" operator
# print(f"Candidiate: {name}\nAge: {age}\nScore: {Score}\nEligible: {eligibility}")  # Prints outs the users details and eligibility status

""" This program will help to screen out all applicants that do not meet up the given conditions and pick only the candidiates that are eligible"""


citizenship = input("Are you a Nigerian: ").strip.lower()
Enrollment = input(" are you an undergraduate student: ").strip.lower()
Scholarship= input( "are currently enjoying any other scholarship?").strip.lower()
Academic_records = int(input("Enter your score in English: "))
Academic_records2 = int(input("Enter your score in Maths: "))
eligibility = (citizenship == "yes") and (Enrollment == "yes") and (Scholarship == "no") and (Academic_records > 70) and (Academic_records2 > 60)
 print(f"You are qualified, {eligibility}")



# Task3: Online Store Cart Calculation**
# - Create a list of items (e.g., "Book", "Pen", "Bag") and another list of prices (e.g., 500, 100, 2000).
# - Start with an empty cart total (cart_total = 0).
# - Use assignment operators (+=) to add the price of some items into cart_total.
# - Print the list of items and the total price using an f-string like this:
# ```
# Items: ['Book', 'Pen', 'Bag']
# Total Price: ₦600

List_items = ["pen", "book", "bag", "textbook", "sharpner", "eraser"]
List_prices = [50, 100, 3000, 1500, 100,  40 ]
Cart_total =0
pen=50
book=100
bag =3000
textbook =1500
sharpner =100
eraser =40
Cart_total += book +pen + textbook
print(f"Items: ['book','pen', 'textbook'] \n Total price: {Cart_total}")


# task4: Student Record**
# - Create an empty dictionary called student.
# - Ask the user to input their name and age, then store them in the dictionary.
# - Add a list of scores (e.g., [70, 85, 90]) to the dictionary.
# - Use a comparison operator to check if the student has passed (average score >= 50). Save the result (True/False) in the dictionary under the key "passed".
# - Use a logical operator to check if the student is a teenager (age between 13 and 19). Save the result as "teenager".
# - Print out the complete record in this format:
# ```
# Student Record:
# Name: John
# Age: 16
# Scores: [70, 85, 90]
# Passed: True
# Teenager: True

Student ={}
User_name = input("Enter your name")
User_age = int(input("Enter your age"))
scores = [ 70, 50, 90,34]
average_score=sum(scores)/len(scores)
Student.update({User_name: User_age})
Student.update({"score":scores})
Student.update({"passed":scores})
passed = (average_score>= 50)
teenager = (User_age > 13 ) and (User_age <= 19)
print(f"Student Record: \n name:{User_name}\n Age:{User_age}\n Scores: {scores}\n passed:{passed}\n teenager{teenager}")



# **Task5: Store Inventory Update**
# - Create a dictionary called store with items and their available quantities. Example:
# store = {"Book": 10, "Pen": 20, "Bag": 5}
# - Ask the user to input the item they want to buy (e.g., "Pen").
# - Ask the user to input the quantity they want to purchase.
# - Use the assignment operator -= to update (reduce) the item quantity in the dictionary.
# - Print the updated dictionary in this format:
# Before purchase: {'Book': 10, 'Pen': 20, 'Bag': 5}
# After purchase: {'Book': 10, 'Pen': 18, 'Bag': 5}
store ={"book": 10, "pen":20, "bag": 50, "pencil":40}
customer_purchase = input("Enter an item you want to buy")
Purchased_quantity =int(input("Enter the quuanity you want"))
Updated_quantity =  (store  -= Purchased_quantity)

print(Updated_quantity)
