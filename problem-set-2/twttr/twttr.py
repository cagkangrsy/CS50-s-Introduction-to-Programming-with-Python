input_text = input("Input: ")
shortened_text = ''

for letter in input_text:
      if letter in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]:
        continue
      else:
          shortened_text += letter
print("Output:", shortened_text)
