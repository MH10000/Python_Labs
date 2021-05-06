'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''
dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}

dict_3 = dict_1.copy()                  # Create a new dictionary with the same contents as dict_1

for x, y in dict_2.items():             # Loop through dict_2  
    if dict_3[x] == x:                  # Trying to only refer to a, b and c here because d doesn't exist in dict_3
        dict_3[x] = y + dict_1[x]       # This keeps giving me a KEY error for d even though I'm specifically trying to have it skip over d :(
    else:
        dict_3[x] = y                   # Tryng to add d and it's value in this else statement

print(dict_3)


