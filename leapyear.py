def leapyear():
    y = int(input("Enter any year: "))
    if y <= 100000 and y >= 1900:
        num = y
        if (num % 4 == 0):
            print("year is even " )
        else:
            print("false")


leapyear()