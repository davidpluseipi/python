# String Methods

course = "Python Programming"

# Convert all the characters of a string to uppercase
print(course.upper())

# Convert all the characters of a string to lowercase
print(course.lower())

# Set only the first characters of each word to uppercase
print(course.title())



# If a string has or may have "white space" or extra spaces...
course = "  Python Programming"
print(course)

# ...use the strip method to remove them.
# lstrip: removes white space from the left
print(course.lstrip())  

# strip removes white space from beginning and end of the string
course = "  Python Programming  "
print(course.strip())

# rstrip: removes white space from the right
course = "Python Programming  "
print(course.rstrip())  



# To find the index of a character or substring in a string
print(course.find("Pro"))
# note the response of -1 here, because the find method is case sensitive
print(course.find("pro"))

# Replace characters or substrings with the replace method
course_lower = course.replace("P", "G")
print(course_lower.find("Gro"))

# To find a character or substring in a string object use the 'in' operator
print("Programming" in course)
print("Programming" not in course)
