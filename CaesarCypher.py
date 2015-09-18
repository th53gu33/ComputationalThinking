message = input("Enter your message: ")
key = int(input("Enter your key: "))
mode = input("Enter if you want to decrypt or encrypt: ").lower()

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ''
message = message.upper()
for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'decrypt':
            num -= key
        if mode == 'encrypt':
            num += key
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)
        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol

print(translated)