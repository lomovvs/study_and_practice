censorship = ['shit', 'fuck']
right_words = ['time', 'god']


def text_censorship(text_split):
    bad_word_caunter = 0
    for word in text_split:
        if word in censorship:
            bad_word_caunter += 1
        else:
            pass
    if bad_word_caunter == 0:
        resultat = 'Проверка пройдена'
    else:
        resultat = 'Проверка не пройдена'
    return resultat


# text = 'a fff ff good fuck d ff c a b'
# text_split = text.split()
# print(text_censorship(text_split))
# text = 'a fff ff good d ff c a b'
# text_split = text.split()
# print(text_censorship(text_split))


# text1 = 'a f'
# text2 = 'ab good'
# text3 = 'fuck d good'
text4 = 'ab d bad'
#
# assert  text_censorship(text1.split()) == 'Проверка не пройдена'
# assert  text_censorship(text2.split()) == 'Проверка пройдена'
# assert  text_censorship(text3.split()) == 'Проверка не пройдена'
assert  text_censorship(text4.split()) == 'Проверка пройдена'