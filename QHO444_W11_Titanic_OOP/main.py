from titanic_data import TitanicData
from titanic_menu import TitanicMenu
from titanic_reports import TitanicReports

def run():
    """ Main application entry point.
        Coordinates data loading, menu selection, and reporting."""

    # Create and load the data
    data = TitanicData()
    data.load("titanic.csv")

    # Create menu and reporting objects
    menu = TitanicMenu()
    reports = TitanicReports(data)

    # Display menu and get user choice
    option = menu.show()

    # Execute the selected option
    if option == 1:
        reports.display_names()
    elif option == 2:
        reports.display_survivors_total()
    elif option == 3:
        reports.display_gender_counts()
    elif option == 4:
        reports.display_age_groups()
    elif option == 5:
        reports.display_survivors_by_age_group()
    else:
        print("Error! Option not recognised!")


# Standard Python entry-point check
if __name__ == "__main__":
    run()
