
# Task1: Fruit collector**
# - Ask the user to enter 5 favourite fruits. Store them in a set and display the set.

fruits = []
fav_fruits= input("Enter five favourit fruits  ").lower()
fruits.append(fav_fruits)
print(set(fruits))


# *Task2: Unique Name Collector**
#  - Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.

seminar = []
name1= input("Enter your name  ")
name2 =input("Enter your name ")
name3 = input( " Enter your name ")
name4 = input( " Enter your name ")
name5 = input( " Enter your name ")
seminar.append(name1)
seminar.append(name2)
seminar.append(name3)
seminar.append(name4)
seminar.append(name5)
print(seminar)
seminar.sort()
print(set(seminar))



# **Task3: Simulate a football match ticket system**
# - Store all seat numbers (1 to 50) in a set
# - Ask users to "book" a seat by entering the number.
# - Remove booked seats from the set.
# - Show remaining seats after each booking.

available_seat =set(range(1,51))
booking=int(input("Welcome !\n Available seats no. 1-50\n Enter your seat no"))
remaining_seat = available_seat.remove(booking)
print(available_seat)
    


# **Task4: Create a Unique Voters Registration System**
# - Ask for voter names and store in a set.
# - If a voter tries to register twice, display a warning.
# - After registration, display the total number of unique voters.


voters_List = []
voters_name1 = input("Enter your name ").title()
voters_name2 = input("Enter your name ").title()
voters_name3 = input("Enter your name ").title()
names= voters_name1, voters_name2, voters_name3
voters_List.append(voters_name1)
voters_List.append(voters_name2)
voters_List.append(voters_name3)
if names in voters_List:
  print("warning:the user you enter already exist!")
print(set(voters_List))



