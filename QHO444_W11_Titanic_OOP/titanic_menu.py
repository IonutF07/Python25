class TitanicMenu:
    """ This class is responsible ONLY for:
        - displaying the menu
        - returning the user's selected option """

    def show(self):
        print()
        print("Please select one of the following options:")
        print("[1] Display the names of all passengers")
        print("[2] Display the number of passengers that survived")
        print("[3] Display the number of passengers per gender")
        print("[4] Display the number of passengers per age group")
        print("[5] Display the number of survivors per age group")
        print()

        # Convert user input from string to integer
        return int(input())
