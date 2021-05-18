'''
Using f-strings, print out the name, last name, and quote of each person in the given dictionary,
formatted like so:

"The inspiring quote" - Lastname, Firstname

'''

famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]
name_ = 0
for quote in famous_quotes:
    if "." in famous_quotes[name_]["full_name"]:
        famous_quotes[name_]["full_name"] = famous_quotes[name_]["full_name"].split(". ")
    else:
        famous_quotes[name_]["full_name"] = famous_quotes[name_]["full_name"].split(" ")
    name_ += 1

name_new = 0
for new_quote in famous_quotes:
    print(f"'{famous_quotes[name_new]['quote']}' - {famous_quotes[name_new]['full_name'][1]}, {famous_quotes[name_new]['full_name'][0]}")
    name_new += 1
