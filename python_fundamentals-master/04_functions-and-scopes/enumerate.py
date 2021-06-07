# Writing the enumerate function from scratch

def my_enumerate(iterable, start=0):
    list_ = []
    x = start
    for item in iterable:
        list_.append((x, item))
        x += 1
    return list_

courses = ['Intro', 'Intermediate', 'Advanced', 'Professional']

for index, course in my_enumerate(courses):
    print(f"{index}: {course} Python")

# OUTPUT:
# 0: Intro Python
# 1: Intermediate Python
# 2: Advanced Python
# 3: Professional Python
