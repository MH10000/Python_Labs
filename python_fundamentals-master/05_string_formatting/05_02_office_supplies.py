'''
Using f-strings, print out the name, last name, and favorite
office supply item of each person in the given dictionary,
formatted like so:

LASTNAME, Name           Office supply item
LONGERLASTNAME, Name     Office supply item

'''

office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]

# Split first and last names to be accessed separately
names_ = 0
for supplies in office:
    office[names_]["full_name"] = office[names_]["full_name"].split(" ")
    names_ += 1

# Use a loop to itterate over the list and print individual items using the fString method
names_3 = 0
for things in office:
    print(f"{office[names_3]['full_name'][1].upper()}, {office[names_3]['full_name'][0]}{' ' * (20 - ((len(office[names_3]['full_name'][0]) + len(office[names_3]['full_name'][1]))))} {office[names_3]['item'].capitalize()}")
    names_3 += 1

