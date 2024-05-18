import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if not re.match(r'\d{1,2}(:\d{2})? (AM|PM) to \d{1,2}(:\d{2})? (AM|PM)', s):
        raise ValueError('Invalid format.')
    times = re.findall(r'(\d{1,2}(:\d{2})?) (AM|PM)', s)
    converted_times = []
    for match in times:
        time, _, period = match
        hour, minute = map(int, (time.split(':') + ['0'])[:2])
        if minute > 59:
            raise ValueError('Invalid minute')
        if period.upper() == 'PM' and hour != 12:
            hour += 12
        elif period.upper() == 'AM' and hour == 12:
            hour = 0
        converted_times.append(f'{hour:02d}:{minute:02d}')
    return f"{converted_times[0]} to {converted_times[-1]}"

if __name__ == "__main__":
    main()
