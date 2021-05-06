'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
occurences = []
# Looks for duplicates
for x in list_:
    count = 0
    for y in list_:
        if y == x:
            count += 1
    occurences.append(count)
# Adds duplicates to a set
duplicates = set()
index = 0
while index < len(list_):
    if occurences[index] != 1:
        duplicates.add(list_[index])
    index += 1

remove_dup = set(list_)                         # Create set from the original list to remove duplicates
uniq_set = remove_dup.difference(duplicates)    # Combine the duplicates set with the original set with duplicates removed to get only unique items
uniq_list = list(uniq_set)                      # Convert the set to a list
print(duplicates)
print(uniq_list)






