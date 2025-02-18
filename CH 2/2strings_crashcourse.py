#STRINGS
#   *this is a data type, a series of characters
#   *anything inside quotes (" ") or (' ') is considered a string in Python
example_string = "a series of characters is a string..."
example_string2 = 'Python is named after "Monty Python" not the snake'

#STRING METHODS
#   *changes the case of words of string
#   *title() method, returns string capitalized
#   *upper() method, returns all characters of string capitalized
#   *lower() method, returns all characters of string lowercase
#       *useful in data storage (removes errors from miscapitalization)
first_programmers_name = "ada lovelace"
print(first_programmers_name.title())
print(first_programmers_name.upper())
print(first_programmers_name.lower())

#VARIABLES INSIDE STRINGS
#   *place letter 'f' immediately before opening quotation mark
#   *use brackets to call the variable you want called inside string
#   *these are called f-strings which are used to compose complete messages
first_name = "ada"
last_name = "lovelace"
message = f"{first_name} {last_name}!"
print(message.upper())

#ADDING WHITESPACE
#   *whitespace: any nonprinting characters
#   *(\t) used to add a tab space to text
#   *(\n) used to add a newline to text
#   *these escape characters will be useful when writing complex lines of code
example_string3 = "MJ was here\n\t MJ was also here\n"


#STRIPPING WHITESPACE
#   *often want to compare strings
#   *sometimes strings include whitespace, which changes the value of the string
#   *in order to properly compare values

#   *(rstrip) method strips right side of string
#   *(lstrip) method strips left side of string
#   *(strip) method strips both sides of string
#   *these methods are used to clean up user input

favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())


#REMOVING PREFIXES
#   *(removeprefix) method removes the part of string you need changed
ex_url = "https://www.google.com"
print(ex_url.removeprefix('https://'))

#AVOIDING SYNTAX ERRORS WITH STRINGS
#   *sometimes an apostrophe is mistaken as a single quote
#   *interpreter doesn't recognize the character (') as valid Python code
#   *can use the escape character (\) to mitigate errors
example_string4 = 'me and mine\'s'
print(example_string4)

