import csv

with open('Word Frequencies(lists)\input1.csv', 'r') as file:
    file_reader = csv.reader(file)
    
    words = []

    for row in file_reader:
        for word in row:
            words.append(word)

word_dict = {}

for word in words:
    if word in word_dict.keys():
        word_dict[word] = word_dict[word] + 1
    else:
        word_dict[word] = 1

for word in word_dict.keys():
    print(word, '-', word_dict[word])