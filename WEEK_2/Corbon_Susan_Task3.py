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


# TASK2
text =  "I love Python"  # No.6 ( using the in function to check a sub-string (Python) in a string)
print("Python" in text) 

text =input("enter a word")  # No.7 ( reversing an input with reverse indexing)
print(text[::-1])

text= "      dance      "   #  No.8 ( Removing leading and trailing space with strip())
print(text.strip())


text = input("make a sentence")     # no 9 counting the number of vowels in a sentence using sum of characters and 'in'function
vowel = "aeiouAEIOU"
count_vowel = sum(1 for char in text if char in vowel)
print(count_vowel)


Num = int("1234")  # No.10 convert a string to an integer and multiplying by 2
print(Num *2)


#task3 
fruits = "apple,banana,orange,pinapple"   # No.11 using the split() to separate each fruit into a list
print(fruits.split( ",")) 


sentence = input("enter a sentence")       #No.12 Spliting the words in a sentence by using split()
[print(word) for word in sentence.split()]


sentence= "we are all in it"        # No.13  repalcing whitespaces with _
print(sentence.replace(" " ,"_"))


fruit= "banana"             # No.14 using the count() to count the number of a in the string banana
print(fruit.count("a"))


website = "https://dances.com"    # No. 15 using the startwith () to check if https:// is at the beginning of a string
print(website.startswith("https://"))




