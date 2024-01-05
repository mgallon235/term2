## List comprehension

sample = ['doctor','enfermera','animales','cuchino']

# return a new list with the first character of each object in the sample list
result = [sam[0] for sam in sample]
result

# Create list comprehension: squares
squares = [i**2 for i in range(0,10)]
squares

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0,5)] for row in range(0,5)]
# Print the matrix
for row in matrix:
    print(row)

#----------------------------------------------------------- Advanced list comprehension

# Adding conditions to list comprehension
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member)>=7]
# Print the new list
print(new_fellowship)

# Another example where we only consider those with len >= 7 else empty space
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
# Create list comprehension: new_fellowship
new_fellowship = [member if len(member)>=7 else '' for member in fellowship]
# Print the new list
print(new_fellowship)

#Another example iterating over a dictionary
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}
# Print the new dictionary
print(new_fellowship)