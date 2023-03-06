
SYMBOLS ='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Вы хотите зашифровать или расшифровать текст?')
        mode = input().lower()
        if mode in ['зашифровать', 'з', 'расшифровать', 'р']:
            return mode
        else:
            print('Введите "зашифровать" или "з" что бы зашифровать. Для расшифровки введите "расшифровать" или "р"')

def getMessage():
    print('Введите текст:')
    return input()

def getKey():
    while True:
        print(f'Введите ключ шифрования от 5 до {MAX_KEY_SIZE}')
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'p':
        key = -key
    translater = ' '
    for symbol in message:
        symbol_index = SYMBOLS.find(symbol)
        if symbol_index == -1:
            translater += symbol
        else:
            symbol_index += key
            if symbol_index >= len(SYMBOLS):
                symbol_index -= len(SYMBOLS)
            elif symbol_index < 0:
                symbol_index += len(SYMBOLS)
            translater += SYMBOLS[symbol_index]
    return translater

mode = getMode()
message = getMessage()
key = getKey()
print('Преобразованный текст:')
print(getTranslatedMessage(mode, message, key))















