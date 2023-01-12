import struct
import codecs
import random

F = open('D:\J\data.txt', 'w')
F.write("how ol day you\n")
F.write('world\n')
a = random.randint(1, 2)
print(a)
if a == 1:
    F.close()
if a == 2:
    F = open('D:\J\data.txt', 'w')
    text = F.readline()
    text.split()
    print(text)
dir(F)
help(F.seek)


text = 'code'
text.encode('D:\J\data.txt', 'utf-8')

s = 'sp\xc4m'
print(s)
file = open('D:\J\data.txt', 'w', encoding='utf-8')

file.close()

text = open('D:\J\dataa.txt', encoding='utf-8').read()
print(text)

raw = open('D:\J\dataa.txt', 'rb').read()
len(raw)
text.encode('utf-8')
raw.decode('utf-8')
print(raw)


open('unidata.txt', 'rd').read()
open('unidata.txt').read()

codecs.open('unidata.txt', encoding='utf-8').read()