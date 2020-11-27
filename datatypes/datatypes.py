# Strings
str0 = "It's a boy!"
str1 = 'Correct'

# Integer (int)
num0 = 25
print(num0)
print(type(num0))

# Decimal (float)       # upto 15 decimal places
num1 = 25.0
print(num1)
print(type(num1))

# Complex Number (complex)
num2 = 4 + 3j
print(num2)
print(type(num2))

# List                  # lists are 0 based
empty = []
ints = [1, 2, 3]
mixed = ['my', "hi there", 3.4]
list_with_list = ['oh', mixed]
the_list = ['a','b','c','d','e']

# Indexing
print(the_list[0]) # prints a
print(the_list[1]) # prints b
print(the_list[2]) # prints c

the_list[3] = 'p'

# Negative Indexing
print(the_list[-2])

# Nested List
print(mixed)
print(list_with_list[1][2])
print(list_with_list)

# Slicing using the 'slice' operator (:)
print(the_list[1:3])
print(the_list[:]) # prints all elements

# Appending 
# one element at a time
the_list.append('f')
print(the_list)

# Extending
# multiple elements at once
the_list.extend(['g','h','i'])
print(the_list)

# Adding list together
just_kidding = ['j','k']
print(the_list + just_kidding)

# Multiplying elements in a list
test = ['testing 1, 2, 3']
broadcast = test*3
print(broadcast)

# Inserting elements into a list
str = ['I ', 'know.']
str.insert(1, "don't ")
print(str)

counter = [0b00, 0b01, 0b100]
print(counter)
counter[2:2] = [0b10, 0b11]
print(counter)

#del
#remove
#pop
#clear
#index
#sort
#reverse
#copy