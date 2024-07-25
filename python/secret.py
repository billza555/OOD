def checkCharacter(characters):
    max = 0
    dictCharacter = {}
    returnCharacter = []
    for character in characters:
        if character not in dictCharacter:
            dictCharacter[character] = 1
        else:
            dictCharacter[character] += 1
        if dictCharacter[character] > max:
            max = dictCharacter[character]
    if max == 1:
        return returnCharacter
    for character in dictCharacter:
        if dictCharacter[character] == max:
            returnCharacter.append(character)
    return returnCharacter

def bon(w):
    characters = checkCharacter(w)
    number = 0
    for character in characters:
        number += ord(character) - ord('a') + 1
    return number * 4

secretCode = input("Enter secret code : ")
print(bon(secretCode))
