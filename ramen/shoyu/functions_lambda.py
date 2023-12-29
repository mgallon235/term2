import pandas as pd

## Using .keys() module to print indexes.
## Helps when iterating on DataFrame columns
#### Doesn't work with lists
lista = pd.Series([1,2,3,4,5,6,7])
for i in lista.keys():
    print(i)

### This example might not be usable given that this can be calculated with a frequency table
# Create a series of languages
lang = pd.Series(['en','en','en','it','en','pe','en','en','en','pe'])
# Initialize an empty dictionary: langs_count
langs_count = {}
# Iterate over lang column in DataFrame
for entry in lang:
    # If the language is in langs_count, add 1 
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1
# Print the populated dictionary
print(langs_count)


#--------------------------------------------Lambda functions

#Defining a simple lambda function
add_bangs = (lambda a: a+'!!!')
add_bangs('hello')

# .map(function,sequence)

nums = [32, 2, 56, 7, 9, 11]

#this will print a map object not a list
mult_2 = map(lambda x: x*2,nums)
#which is why we need to do some transfromations
list(mult_2)


#---------------------------------------------Lambda function with filter()
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member)>6, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Print result_list
print(result_list)

#----------------------------------------------- reduce()
'''The reduce() function is useful for performing some computation on a list and, 
unlike map() and filter(), returns a single value as a result. To use reduce(), 
you must import it from the functools module.'''

# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""
    hodgepodge = ''
    for word in args:
        hodgepodge += word
    return hodgepodge

## This is how this would be done using the reduce function
# Import reduce from functools
from functools import reduce
# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']
# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1+item2, stark)
# Print the result
print(result)


#-----------------------------------------------------Error Handling
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Initialize empty strings: echo_word, shout_words
    echo_word = ""
    shout_words= ""
    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1*echo
        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word+'!!!'
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")
    # Return shout_words
    return shout_words
# Call shout_echo
shout_echo("particle", echo="accelerator")


## Another example:
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo <0:
        raise ValueError('echo must be greater than or equal to 0')

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo
shout_echo("particle", echo=5)
#------------------------------------------------ Example

## example working with a dataset twitter
# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2]=='RT', tweets_df['text'])
# Create list from filter object result: res_list
res_list = list(result)
# Print all retweets in res_list
for tweet in res_list:
    print(tweet)