userInput = input("Enter your sentence: ")

vowels = "AEIOUaeiou"
consonants = "bcdfghjklmnpqrstvwxyx"
consonants += consonants.upper()

displayVowels = ""
displayConsonants = ""
displayPunctuation = ""

for letter in userInput:
    if letter in vowels:
        displayVowels += letter
    elif letter in consonants:
        displayConsonants += letter
    else:
        displayPunctuation += letter


print("Vowels: " + displayVowels)
print("Consonants: " + displayConsonants)
print("Punctuation: " + displayPunctuationH)