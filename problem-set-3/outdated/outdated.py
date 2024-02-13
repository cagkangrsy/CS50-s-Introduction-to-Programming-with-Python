months_dict = { "January":1,
          "February":2,
          "March":3,
          "April":4,
          "May":5,
          "June":6,
          "July":7,
          "August":8,
          "September":9,
          "October":10,
          "November":11,
          "December":12
}

while True:
    try:
        date = input("Date: ").strip()
        if date[0].isdigit():
            elements = date.split('/')
            if int(elements[0]) > 12 or int(elements[1]) > 31:
                continue
            else:
                print(f"{elements[2]}-{int(elements[0]):02}-{int(elements[1]):02}")
                break
        else:
            if ',' not in date:
                continue
            else:
                elements = date.replace(',', '').split(' ')
                if months_dict[elements[0]] > 12 or int(elements[1]) > 31:
                    continue
                else:
                    print(f"{elements[2]}-{months_dict[elements[0]]:02}-{int(elements[1]):02}")
                    break
    except EOFError:
        print()
        break
    except ValueError:
        pass
