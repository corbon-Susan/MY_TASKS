#**Tuple Practice**
# **Task1:  Create and Display**
# - Ask the user to enter three favorite Nigerian dishes (one at a time).
#  - Store them in a tuple called dishes.
# - Print the tuple in a single line, separating items with commas.
# - Use the \n escape sequence to print each dish on a new line.

Meal_1=(input("Enter you favourite nigerian food"))
Meal_2 = (input("Enter another meal"))
Meal_3 =(input(" enter the third meal"))
meals = (Meal_1 +" " + Meal_2 + " " +Meal_3).split()     # used split () to split out the foods the use entered
meal_tuple = tuple(meals)
print(meal_tuple)
print(type(meal_tuple))
print(meal_tuple)
for meal in meal_tuple:          # for used to call out all the meals in the tuple
    print(meal) 


# **Task2: Tuple and Input**
# - Ask the user for 5 best friends’ names.
# - Store them in a tuple friends.
# - Print the tuple in reverse order.

names=input(("enter the 5 names of your best friends"))      # to get the five names of the friend
T_name =names.split()                                     # split the names in the list
Tuple_name = tuple(T_name)                                 # change the list to a tuple
print(Tuple_name[::-1])        # print the name from the last name to the first name
print(type(Tuple_name))      # check the data types


# **Task3: Tuple Operations**
# - Create a tuple of 5 Nigerian states entered by the user.
#   - Print the first state and last state.
#   - Check if "Lagos" is in the tuple and print "Yes" or "No".
#   - Print the number of states entered.
#     - (Hint: use the tuple membership)

States=input(("Enter the names  of five states in Nigeria"))   #collects five states from the user
T_States= States.split()            #spliting the user input by using the split()
Tuple_States= tuple(T_States)       #change the string to tuple
print((Tuple_States [0:5:4]))      # print the first and the last name using indexing
print("lagos" in Tuple_States)     # checking if lagos is among the users inputed

# **Task4: Tuple Unpacking**
#  - Ask a user for their;
#   - First name
#   - Age
#   - Favorite color
#   - Home town
#   - Store them in a tuple profile and unpack into variables.
#   - Print and use  escape sequence to align each piece of information nicely.

person_info =input("your first name,age,favourite color, home town")  #collects user input 
print(person_info)                                                  #print user input
person_profile=person_info.split()                              #
person_profile2 = tuple(person_profile)
name, age, colour, town = person_profile2
print(f"name:", "\t" "\t", name)
print(f"age:",  "\t" "\t", age, )
print(f"colour:","\t", colour)
print(f"home town:" "\t", town)   
print(type(person_profile2)) 


# **Task5: Modify Tuple Indirectly**
# Ask a user to enter three items for their shopping list.
#   - Store in a tuple shopping_list.
#   - Convert it to a list, then ask for two more items to add.
#   - Convert back to a tuple and print the updated list using join() to display items separated by " | ".
 
Shopping_list= input("Enter three items of your choice")
shopping_list2= (tuple(Shopping_list.split()))
More_shopping_list = input("two more items")
new_shopping_list = (tuple(More_shopping_list.split()))
new_shopping_list2 = new_shopping_list + shopping_list2
full_shopping_list = tuple(new_shopping_list2)
print("Your List of items are", "|".join(full_shopping_list)) 
print(type(new_shopping_list2))


# **Task6: Attendance Tracker**
# - Write a Python program that;
#  - Stores the days of the week in a tuple.
#  - Stores the months of the year in another tuple.
#  - Asks the user to enter:
#    - Student’s name
#    - Gender
#    - Course Track  
#    - Current month number (1-12)
#    - Current day number (1-7)

Week_days= ( "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
Month = ("Jan.", "Feb.","March", "April", "May", "June","July", "August", "Sept.", "Oct.", "Nov.","Dec")
Student_details =input("Enter your name, gender, course")
name, gender, course =  Student_details.split() 
print(Student_details)
current_month_number =int(input("enter current month number"))
current_day_number = int(input("current day number"))
current_month_number = current_month_number-1
current_day_number = current_day_number-1
print(f"Name:{name}, Gender:{gender}, course:{course}, you are present on  {Week_days[current_day_number]}, in {Month[current_month_number]}")
