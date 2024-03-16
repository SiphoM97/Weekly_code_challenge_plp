# Write a program that accepts user input to create a list of integers.
# Then, compute the sum of all the integers in the list.

# Accept user input to create a list of integers
user_input = input("Enter a list of integers separated by spaces: ")
integer_list = [int(x) for x in user_input.split()]

# Compute the sum of all the integers in the list
sum_of_integers = sum(integer_list)

# Print the sum of all the integers
print("Sum of integers:", sum_of_integers)

# Create a tuple containing the names of five of your favorite books.
# Then, use a for loop to print each book name on a separate line.

books = ("A shoe dog", "lean start", "Good to great", "zero to one", "The kyablion")
for book in books:
        print(book)

# Write a program that uses a dictionary to store information about a person,
# such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary.
# Then, print the dictionary to the console.

name = input("Enter your name")
age = input("Enter your age")
fav_book = input("Whats your favourite book?")

personal_info = {
    name: name,
    age : age,
    fav_book : fav_book,
}

print(personal_info)