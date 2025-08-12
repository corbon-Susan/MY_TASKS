#TASK 1
name =input("Enter your name")  # No.1 -changing to uppercase
print(name.upper())

text= "Python"   # No.2 using string index to get the first and last character
print(text [0:6:5])


name =input("what is your name") # No.3 asking a user for their name and print hello with user input
print(f"Hello {name}")

text = "  I love Python"      # no 4 counting the number of a letters in a string using sum of characters and isalpha()
count = sum(1 for char in text if char.isalpha())
print(count)


word = "Hello World"            # no.5 Using the replace function to change a string
print(word.replace("World", "python"))
