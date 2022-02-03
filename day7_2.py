censorship = ['shit', 'fuck']
right_words = ['time', 'god']

bad_word_caunter = 0

text = 'a fff ff good d ff c a b'
text_split = text.split()

for word in text_split:
    if word in censorship:
        bad_word_caunter += 1
    else:
        pass

if bad_word_caunter == 0:
    print('Текст не нуждается в редактировании', '\n', text)
else:
    print('Текст содержит нецензурные слова и нуждается в редактировании')
# i = 0
# print(word_filter(text))
# for i in 4
# text1 = 'a f'
# text2 = 'ab good'
# text3 = 'a d good'
# text4 = 'ab d bad'
#
# assert  shimpfen(text) == 'Проверка не пройдена'
# assert  shimpfen(text) == 'Проверка пройдена'
# assert  shimpfen(text) == 'Проверка не пройдена'
# assert  shimpfen(text) == 'Проверка не пройдена'
