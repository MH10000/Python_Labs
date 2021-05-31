'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
list_words = []
with open("words.txt", "r") as fin:
    for word in fin.readlines():
        word = word.rstrip()
        list_words.append(word)

list_words.sort(key=len)

for short in list_words:
    if len(short) == len(list_words[0]):
        print(short)

for long in list_words:
    if len(long) == len(list_words[-1]):
        print(long)

print(len(list_words))