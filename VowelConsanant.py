userInput = input("Enter your sentence: ")

vowels = "AEIOUaeiou"

displayVowels = ""
displayConstanants = ""

for letter in userInput:
    if letter in vowels:
        displayVowels += letter
    else:
        displayConsanants += letter

print("Vowels: " + displayVowels)
print("Consonants: " + displayConsonants)