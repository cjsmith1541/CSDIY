def main():
    answer = convert(input("What time is it? "))
    if answer >= 7 and answer <= 8:
        print("breakfast time")
    elif answer >= 12 and answer <= 13:
        print("lunch time")
    elif answer >= 18 and answer <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + (((100 / 60) * float(minutes)) / 100)

if __name__ == "__main__":
    main()