#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in December 2020
# Program displaying a month based on an inputted integer


def main():
    # Program displaying a month based on an inputted integer

    print("Give me an integer and I'll give you a month!")

    # Input
    month = int(input("Please enter an integer: "))

    # Process
    if month == 1:
        # Output
        print("January")
    elif month == 2:
        # Output
        print("February")
    elif month == 3:
        # Output
        print("March")
    elif month == 4:
        # Output
        print("April")
    elif month == 5:
        # Output
        print("May")
    elif month == 6:
        # Output
        print("June")
    elif month == 7:
        # Output
        print("July")
    elif month == 8:
        # Output
        print("August")
    elif month == 9:
        # Output
        print("September")
    elif month == 10:
        # Output
        print("October")
    elif month == 11:
        # Output
        print("November")
    elif month == 12:
        # Output
        print("December")
    else:
        # Output
        print("This integer does not correspond to a month")


if __name__ == "__main__":
    main()
