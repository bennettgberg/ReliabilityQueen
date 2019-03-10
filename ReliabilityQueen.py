#This program will be a laundry app that works better than "Speed Queen", the system currently used by Rutgers.

def main():
    print("Welcome to ReliabilityQueen. It's a laundry app like SpeedQueen (the app used by Rutgers), but way better!")
    username = raw_input("Please enter a username: ")
    password = raw_input("Please enter a password: ")
    location = raw_input("Please enter your building location: ")
    machine = raw_input("Please enter what machine you would like to use: ")
    print("Thank you for using ReliabilityQueen. This app did not do anything useful. "
            + "\nHowever, it did not take your personal information and leave it susceptible to being stolen, "
            + "\nand it did not deduct money from your account without actually washing/drying your clothes. "
            + "\nIn addition, there were no error messages erroneously printed. "
            + "\nFor all of these reasons and more, ReliabilityQueen is a much better laundry app than SpeedQueen.")


if __name__ == "__main__":
    main()
