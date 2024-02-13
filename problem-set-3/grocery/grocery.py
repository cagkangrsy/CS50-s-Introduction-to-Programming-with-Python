grocery_list = []

while True:
    try:
        item = input()
        grocery_list.append(item)
    except EOFError:
        print()
        break
    except KeyError:
        pass

items_dict = dict((element,grocery_list.count(element)) for element in set(grocery_list))
sorted_dict = dict(sorted(items_dict.items()))

for key in sorted_dict:
    print(sorted_dict[key], key.upper())
