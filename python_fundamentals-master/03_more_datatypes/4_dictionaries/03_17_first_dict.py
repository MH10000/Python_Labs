'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''
dict_ = {}
x = 1
y = 1
z = 1
dict_[x] = y
while z < 11:
    y = x * x
    dict_.update({x: y})
    x += 1
    z += 1

print(dict_)


