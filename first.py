symb_with_space = 0
space = 0
word = 0
str = 0
punc = '.,;:"-()?'
sentence_punc = '.!?'
count_punc = 0
count_sentence = 0
file = open('text.txt', encoding='utf-8')
for row in file:
    str += 1
    for letter in row:
        symb_with_space += 1
        if letter == ' ':
            space += 1
        for i in punc:
            if letter == i:
                count_punc += 1
        for i in sentence_punc:
            if letter == i:
                count_sentence += 1

symb = symb_with_space - space
symb_without_punc = symb_with_space - count_punc
word = space + str
file.close()
print('символов вместе с пробелами', symb_with_space)
print('символов без пробела', symb)
print('символов без знаков препинания', symb_without_punc)
print('количество слов', word)
print('количество предложений', count_sentence)
