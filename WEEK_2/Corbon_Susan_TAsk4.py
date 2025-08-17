# Task1: Your Favorite Life Quote**
# - Ask the user to input their favorite quote.
# - Convert it to title case.
# - Print it with quotation marks using escape sequences.

Fav_quote =input(str("write down your favourit quote"))
Fav_quote2= (Fav_quote).title()
print(f" \" " ,Fav_quote2, " \" ")


#Task2
# - Create an empty list.
# - Ask the user to enter 3 shopping items (one by one).
# - Add them to the list.
# - Display the list as a single string, separated by commas.

Shopping_list =[]
item1 =input("pick an item")
Item2 = input("pick a second item")
Item3 = input("pick another item")
Shopping_list.append(item1)                 #add users items to empty shopping list
Shopping_list.append(Item2)
Shopping_list.append(Item3)
Shopping_list2=(Shopping_list)
print(f"Your shopping list:",Shopping_list2)
print(type(Shopping_list2)) 


# **Task 3: Word Counter**
# - Ask the user for a sentence.
# - Split the sentence into a list of words.
# - Print how many words are in the sentence.

Sentence =input (" Enter a sentence")
Sentence1 = list(Sentence)
words = Sentence.split()            # split method to separate the words in the sentence
words2 = len(words)   # len () to count the number of words in the user input
print(words2)  #print the number of words


# **Task 4: Name Organizer**
# - Ask the user to enter 5 names (separated by spaces).
# - Convert all names to lowercase.
# - Sort the list alphabetically.
# - Display them one name per line.
#   -Tips: use `range()`,`sort()`, `for`, `in`, `split()`, `len()`,`lower()` 

names=input("Enter five names: ").lower()
#print(names)
names1=names.split()
names1.sort()
for i in range(len(names1)):
    print(names1[i])



# **Task 5: Student Score Tracker**
# - Ask the user for 3 student names.
# - For each student, ask for their score.
# - Store the results in two lists (one for names, one for scores).
# - Print a formatted output showing Name — Score, aligned neatly.
#   - Tips: You are to start by creating two empty lists.

List1 = []
List2 =[]
Student_names=(input(" Enter three student names"))
Student_scores =(input("Enter student scores"))
List1.append (Student_names)
List2.append(Student_scores)
for i in range(1):
    print(f"{List1[i]}: \t{List2[i]}")


# **Task 6: Word Analyzer**
# - Ask the user to input a word.
# - Print the length of the word.
# - Check if it is all uppercase, all lowercase, or title case.
# - Reverse the word using slicing.

word =input ("Enter a word")
word_count= len(word)
print(word_count)
print(word.isupper())
print(word.islower())
print(word.istitle())
print(word[::-1])


# **Task 7: List Manipulation**
# - Create a list of five cities.
# - Replace the third city with a new one (entered by the user).
# - Remove the last city.
# - Add a new city to the beginning of the list.
# - Print the updated list.

Cities=["New York, London, Abuja, Paris, Abidjan"]
print(Cities)
new_city=input("Enter a new city to replace the third city")
Cities2= Cities.append(new_city)
print(Cities)
Cities2= Cities.pop(-1)
print(Cities2)


