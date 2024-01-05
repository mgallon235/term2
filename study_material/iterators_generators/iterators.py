# Create a range object: values
values = range(10,20)
# Print the range object
print(values)
# Create a list of integers: values_list
values_list = list(values)
# Print values_list
print(values_list)
# Get the sum of values: values_sum
values_sum = sum(values)
# Print values_sum
print(values_sum)

#-----------------------------iterables and iterators
## creating an iterator
samples = ['hello','hola','kkj','ppp']

sample_it = iter(samples)

print(next(sample_it))
print(next(sample_it))
print(next(sample_it))
print(next(sample_it))

### this is the same as running a for loop over samples

for i in samples:
    print(i)

#-------------------------------------- Using Enumerate()
#creates an object which includes the values of the lists with their respective index number
samples = ['hello','hola','kkj','ppp']

e = enumerate(samples)
#if we transform the enumerate objecte that we created, we get a list of tuples
list(e)

##Exercise:
##iterating over a enumerate object:

for index, value in enumerate(samples):
    index = index+1
    print(index,value)

##Exercise:
for index, value in enumerate(samples,start=20):
    print(index,value)

#--------------------------------------------------------------------zip()

samples = ['hello','hola','kkj','ppp']
samples2 = ['mikel','josefina','karem','miguel']

for a , z in zip(samples,samples2):
    print(a,z)

# if you create an object using zip, when printed, you'll get a list of tupples with a value of each list

zlist = zip(samples,samples2)
print(list(zlist))
print(*zlist)

#Exercise:
# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants,aliases,powers))
# Print the list of tuples
print(mutant_data)
# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants,aliases,powers)
# Print the zip object
print(mutant_zip)
# Unpack the zip object and print the tuple values
for value1,value2,value3 in mutant_zip:
    print(value1, value2, value3)


#Exercise:
samples = ['hello','hola','kkj','ppp']
samples2 = ['mikel','josefina','karem','miguel']

# Create a zip object from mutants and powers: z1
z1 = zip(samples,samples2)
# Print the tuples in z1 by unpacking with *
print(list(zip(*z1)))
# Re-create a zip object from mutants and powers: z1
z1 = zip(samples,samples2)
# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)
# Check if unpacked tuples are equivalent to original tuples
print(result1 == samples)
print(result2 == samples2)

result1
samples


#-------------------------------------UseCase, loading large datasets in Chunks
import pandas as pd

#Exercise: Create a dictionary with counts of entries in 
# Initialize an empty dictionary: counts_dict
counts_dict = {}
# Iterate over the file chunk by chunk
for chunk in pd.read_csv('tweets.csv',chunksize=10):
    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)


#Exercise: Creating a function
#Define count_entries()
def count_entries(csv_file,c_size,colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file,chunksize=c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict
# Call count_entries(): result_counts
result_counts = count_entries('tweets.csv',10,'lang')
# Print result_counts
print(result_counts)
