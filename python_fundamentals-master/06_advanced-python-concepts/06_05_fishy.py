# Using a listcomp, create a list from the following tuple that includes
# only words ending with -fish. Tip: Use an `if` statement in the listcomp.

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

list_fish = [x for x in fish_tuple if x[-4:-1] == "fis"]
print(list_fish)