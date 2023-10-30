Python Program to Count the Number of Occurrence of a Character in String
Example 1: Using a for loop
count = 0

my_string = "Programiz"
my_char = "r"

for i in my_string:
    if i == my_char:
        count += 1

print(count)

Example 2: Using method count()
my_string = "Programiz"
my_char = "r"

print(my_string.count(my_char))

