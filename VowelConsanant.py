userInput = input("Enter your sentence: ")

vowels = "AEIOUaeiou"
consanants = "bcdfghjklmnpqrstvwxyx"
consanants += consanants.upper()

fvowels = ""
fconstanants = ""

for letter in userInput:
    if letter in vowels and consanants:
        displayVowels += letter
        displayConsanants += letter

print("Vowels: " + displayVowels)
print("Consonants: " + displayConsonants)