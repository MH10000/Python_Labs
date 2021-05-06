'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5]

set_ = set((list_))
list_ = list(set_)
print(list_)
