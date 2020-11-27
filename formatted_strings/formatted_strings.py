first = "David"
last = "Meissner"
# Using concatenation
full = first + " " + last
print(full)

# Using formatted strings
full = f"{first} {last}"  # the f can be lower or uppercase
print(full)

# The formatted string can contain any valid expression
full = f"{len(first)} {2 + 2}"
print(full)
