def get_alphabet(words):
    for word in words:
        if word.isalpha():
            return ord(word)
        
def shell_sort(numbers):
    gap = len(numbers)
    while gap != 1:
        gap = gap // 2 + gap % 2
        for index in range(len(numbers)):
            if index + gap >= len(numbers):
                break
            if get_alphabet(numbers[index]) > get_alphabet(numbers[index + gap]):
                number = numbers[index + gap]
                numbers[index + gap] = numbers[index]
                numbers[index] = number
    return numbers

words = input("Enter Input : ").split()
for word in shell_sort(words):
    print(word, end=" ")
print()