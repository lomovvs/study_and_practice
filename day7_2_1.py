bad = ['a', 'b', 'c']
good = ['good']
text = 'd ff  good  d a ghgj aa a'
text1 = text
text = text.split()
bad_w_c = 0
bad_w = []
for word in text:
    if word in bad:
        bad_w_c += 1
        bad_w.append(word)
    else:
        pass
if bad_w == 0:
    print('Текст можно читать:', str(text1))
else:
    print('в тексте содежится', bad_w_c, 'ненормативных слова', bad_w)
