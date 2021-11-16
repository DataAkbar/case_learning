# "this is a string."
# 'this is also string.'

# "Changing case in a string with methods"

name = "ada lovely"

print(name.title())

name = "Ada Lovelace"

print(name.upper())
print(name.lower())

""" Combining or Concatenating Strings"""

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print("Hello, " + full_name.title() + "!")

# method 2
message = "Hello, " + full_name.title() + "!"
print(message)

""" Adding Whitespace to String with Tabs or NewLines """

print("Python")
print('\tpython')
print('Languages:\nPython\nC\nLavaScript')
print("____________________")
print('Languages:\n\tPython\n\tC\n\tLavaScript')


"""Stripping Whitespace"""

# favorite_language = "python "
# favorite_language = favorite_language.rstrip()
# print(favorite_language)


"""Adding syntax Errors eith String"""
message_1 = "One of Python's ..."
print(message_1)

# message_1 = 'One of Python's ...' # kod ISHLAMIDI
# print(message_1)



