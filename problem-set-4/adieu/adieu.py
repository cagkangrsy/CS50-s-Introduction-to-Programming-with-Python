import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ").strip().lower()
        names.append(name.capitalize())
        people = p.join(tuple(names))
    except EOFError:
        print()
        break
print("Adieu, adieu, to", people)
