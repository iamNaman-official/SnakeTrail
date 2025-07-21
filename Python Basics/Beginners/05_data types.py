# Strings.
# Subscripting :
# Indexing starts at 0.
print("hello"[0])  # First character
print("hello"[4])
print("hello"[-2]) 

# Integer.
print(123 + 456)

# Large Integer.
print(123_456_789)  
# Python allows underscores for readability.

# Float.
print(3.14159)

#Boolean.
print(True)
print(False)

# Type Error,Checking and Conversion.
# type () : Checking the type of an object.
print(type("Hello"))
print(type(123))
print(type(3.14))
print(type(True))
# type() function returns the type of the object passed to it.
# Conversion functions: int(), float(), str().
# Convert string to integer.
print(int("123")+ int("456"))

name_of_user = input("Enter your name: ")
length_of_name = len(name_of_user)
print(type(name_of_user))
print(type(length_of_name))
print("Your name is " + name_of_user + " and it has " + str(length_of_name) + " characters.")