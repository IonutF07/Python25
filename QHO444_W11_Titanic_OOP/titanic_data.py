import csv


class TitanicData:
    """ This class is responsible ONLY for:
         - loading the Titanic CSV file
         - storing headings and records """

    def __init__(self):
        # List to store column names from the CSV
        self.headings = []

        # List to store all passenger records # Each record is a list of values (strings)
        self.records = []

    def load(self, file_path):
        """ Loads the CSV file into headings and records. """

        # Open the CSV file
        with open(file_path) as file:
            csv_reader = csv.reader(file)

            # First row contains the column headings
            self.headings = next(csv_reader)

            # Remaining rows contain passenger data
            for values in csv_reader:
                self.records.append(values)
