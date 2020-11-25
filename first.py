symb_with_space = 0  # колво символов с пробелами
space = 0  # колво пробелов
word = 0
str = 0
punc = ['.', ',', ';', ':', '...', '!', '-', '"', '(', ')', '?']  # всех знаков препинаний
sentence_punc=['.','...', '!', '?'] #знаки в конце предложения
count_puncuation = 0  # количество знаков препинания
count_sentence = 0 #кол-во предложений
file = open('text.txt', encoding='utf-8')
for row in file:
    str = str + 1
    for letter in row:
        symb_with_space = symb_with_space + 1
        if letter == ' ': space = space + 1
        for i in punc:
            if letter == i: count_puncuation = count_puncuation + 1
        for i in sentence_punc:
            if letter == i : count_sentence=count_sentence+1

symb = symb_with_space - space  # колво символов без пробела
symb_without_punc = symb_with_space - count_puncuation
word = space + str  # так потому что где происходит переход на след страницу нет пробела, поэтому количество таких
                    # переходов равно ( str-1 ), а слов будет ( space+(str-1)+1 = space +str)

print('символов вместе с пробелами', symb_with_space)
print('символов без пробела', symb)
print('знаков без препинания', symb_without_punc)
print('количество слов', word)
print('количество предложений', count_sentence)
