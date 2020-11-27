# Anything inside quotes is considered a string to python, single or double quotes

str0 = 'This is a string.'
str1 = "This is too."

str2 = 'Here I can say that someone told me, "Use quotes properly."'
str3 = "The language of 'Python' is named after Monty Python"


course = "Python Programming"
print(len(course))
print(course[0])
print(course[-2])
print(course[0:3])
print(course[:3])
print(course[0:])
print(course[:])

print(course + course)
print("hey" * 2)
print(("hey " * 2) + "hey!")

# see also:
# string_methods