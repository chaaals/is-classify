from pathlib import Path
import re
from utils.utils import format_name

class Classify:
    def __init__(self, dir: Path):
        self.dir = dir
        self.raw_data = [] # array of sets
        self.redundant_data = {}
        self.categorized_data = { # array of sets for categorize_data
            "name": set(),
            "birthday": set(),
            "email": set(),
            "cell_no": set(),
        }

        # checks if the path exists before reading data sets
        if(dir.is_dir()):
            self.__read_data_sets()
        else:
            raise ValueError('Argument must be a valid directory.')

    def __read_data_sets(self):
        """
        Read the files and in a given dir and stores the value in a 2D array.
        Should not be accessible when an instance is created.
        """ 
        files = [file for file in self.dir.iterdir() if file.is_file()]
        
        for file in files:
            path = self.dir.joinpath(file)
            file_data = set()
            
            with open(path, 'r') as f:
                for line in f:
                    value = line.strip()

                    # counts the number of times the value has ocurred
                    if value in file_data:
                        if self.redundant_data.get(value) is not None:
                            self.redundant_data[value] += 1
                            continue

                        self.redundant_data[value] = 1
                        continue

                    file_data.add(value)
            self.raw_data.append(file_data)
        return self
    
    def get_raw_data(self) -> list[set]:
        """
        Getter fn for raw data
        """
        return self.raw_data
    
    def get_redundant_data(self) -> dict[str:int]:
        """
        Getter fn for redundant data
        """
        return self.redundant_data

    def categorize_data(self):
        """
        Categorize the raw data into "name," "email," "birthday," and "cell_no" lists.
        """

        # Regex for cell numbers, birthdays, and emails
        cell_no_regex = re.compile(r'^\+63-\d{10}$')
        birthday_regex = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        email_regex = re.compile(r'^.+@.+\..{2,}$')

        for data_set in self.raw_data:
            for value in data_set:
                value = value.strip()
                
                if cell_no_regex.match(value):
                    self.categorized_data["cell_no"].add(value)
                elif birthday_regex.match(value):
                    self.categorized_data["birthday"].add(value)
                elif email_regex.match(value):
                    self.categorized_data["email"].add(value)
                else:
                    formatted_name = format_name(value)
                    if formatted_name is not None:
                        self.categorized_data["name"].add(formatted_name)



    def get_categorized_data(self):
        """
        Getter function for categorized data
        """
        return self.categorized_data
    
    def print_categorized_data(self):
        """
        Print categorized data to the terminal
        """
        for category, values in self.categorized_data.items():
            print(f"{category}:")
            for value in values:
                print(f"  {value}")