
en = list(open('words'))
print(type(en))
print(en)
en = [line.rstrip() for line in en]
print(en)
print(type(en))
new = open('words_en.txt', 'w')
for element in en:
    new.write(element + ' ')
new.close()
