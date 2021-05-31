'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''
list_words = []
with open("words.txt", "r") as fin:
    for word in fin.readlines():
        word = word.rstrip()
        list_words.append(word)

list_words.reverse()

with open("revtext.txt", "w") as fout:
    fout.write(f"{list_words}")