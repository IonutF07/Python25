class TitanicReports:
    """ This class is responsible for:
            - analysing the Titanic data
            - printing different reports based on the records """

    def __init__(self, data):
        # data is an instance of TitanicData # We access passenger records through data.records
        self.data = data

    def display_names(self):
        """Print the name of every passenger."""
        for values in self.data.records:
            print(values[3])  # Name is column index 3

    def display_survivors_total(self):
        """Print the total number of survivors."""
        count = 0

        for values in self.data.records:
            # Survived column: 1 = survived, 0 = did not survive
            if int(values[1]) == 1:
                count += 1

        print(count)

    def display_gender_counts(self):
        """Print number of passengers by gender."""
        males = 0
        females = 0

        for values in self.data.records:
            sex = values[4].strip().lower()

            if sex == "male":
                males += 1
            elif sex == "female":
                females += 1

        print(f"females: {females}, males: {males}")

    def display_age_groups(self):
        """ Print number of passengers by age group:
            - children: age < 18
            - adults:   18 <= age < 65
            - elderly:  age >= 65 """

        children = 0
        adults = 0
        elderly = 0

        for values in self.data.records:
            age_text = values[5].strip()

            # Convert age to float (assumes valid data as per original logic)
            age = float(age_text)

            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1

        print(f"children: {children}, adults: {adults}, elderly: {elderly}")

    def display_survivors_by_age_group(self):
        """ Print survivors per age group in the format: survived/total """

        children_total = 0
        adults_total = 0
        elderly_total = 0

        children_survived = 0
        adults_survived = 0
        elderly_survived = 0

        for values in self.data.records:
            age_text = values[5].strip()
            age = float(age_text)
            survived = int(values[1])

            if age < 18:
                children_total += 1
                if survived == 1:
                    children_survived += 1
            elif age < 65:
                adults_total += 1
                if survived == 1:
                    adults_survived += 1
            else:
                elderly_total += 1
                if survived == 1:
                    elderly_survived += 1

        print(
            f"children: {children_survived}/{children_total}, "
            f"adults: {adults_survived}/{adults_total}, "
            f"elderly: {elderly_survived}/{elderly_total}"
        )
