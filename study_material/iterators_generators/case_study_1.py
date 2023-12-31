# Zip lists: zipped_lists
zipped_lists = zip(feature_names,row_vals)
# Create a dictionary: rs_dict
rs_dict = dict(zipped_lists)
# Print the dictionary
print(rs_dict)

#Another example:
# Define lists2dict()
def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""
    # Zip lists: zipped_lists
    zipped_lists = zip(list1, list2)
    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)
    # Return the dictionary
    return rs_dict
# Call lists2dict: rs_fxn
rs_fxn = lists2dict(feature_names,row_vals)
# Print rs_fxn
print(rs_fxn)


# Another example: Using previous function**
# Print the first two lists in row_lists
print([row for row in row_lists[0]])
print([row for row in row_lists[1]])
# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names,sublist) for sublist in row_lists]
# Print the first two dictionaries in list_of_dicts
print([row for row in list_of_dicts[0]])
print([row for row in list_of_dicts[1]])


#Another example: 
# Import the pandas package
import pandas as pd
# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]
# Turn list of dicts into a DataFrame: df
df = pd.DataFrame(list_of_dicts)
# Print the head of the DataFrame
print(df.head())