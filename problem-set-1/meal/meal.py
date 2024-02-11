def main():
    hours = convert(input("Enter the time in '##:##' format: "))
    if hours >= 7 and hours <= 8:
        print("breakfast time")
    if hours >= 12 and hours <= 13:
        print("lunch time")
    if hours >= 18 and hours <= 19:
        print("dinner time")


def convert(time):
    if 'a.m.' in time:
        time = time.strip(" a.m.")
        time_list = time.split(":")
        hours = float(time_list[0]) + (float(time_list[1]) / 60)
    elif 'p.m.' in time:
        time = time.strip(" p.m.")
        time_list = time.split(":")
        hours = (12.0 + float(time_list[0])) + (float(time_list[1]) / 60)
    else:
        time_list = time.split(":")
        hours = float(time_list[0]) + (float(time_list[1]) / 60)
    return hours


if __name__ == "__main__":
    main()
