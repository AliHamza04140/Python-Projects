def main():
    time = input("What time is it? ")
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        print("")


def convert(n):
    hours, minutes = n.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + minutes / 60

main()