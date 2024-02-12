input_string = input("Write the word in camel case (camelCase)")
word = ''
words = []

for char in input_string:
    if char.isupper():
        words.append(word)
        word = char
    else:
        word += char
words.append(word)

snake_case = ''
for element in words:
    snake_case += element.lower() + '_'
snake_case = snake_case[:-1]

print(snake_case)
