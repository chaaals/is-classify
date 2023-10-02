from pathlib import Path
import re

class Classify:
    def __init__(self, dir: Path):
        self.dir = dir
        self.raw_data = [] # array of sets
        self.redundant_data = {}
        self.categorized_data = { # array of lists for categorize_data
            "name": [],
            "birthday": [],
            "email": [],
            "cell_no": [],
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
    
    def format_name(self, name_str):
        parts = name_str.split()

        # Check if there are at least two parts (first name and last name)
        if len(parts) >= 2:
            first_name = parts[0]
            last_name = parts[-1]  # Use the last part as the last name


        # Check if there are at least three parts (first, middle, last names)
        if len(parts) >= 3:
            middle_name = parts[1]
            middle_initial = middle_name[0]
            formatted_name = f"{last_name}, {first_name} {middle_initial}."
        else:
            formatted_name = f"{last_name}, {first_name}"

        return formatted_name
    
        return None


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
                if cell_no_regex.match(value):
                    self.categorized_data["cell_no"].append(value)
                elif birthday_regex.match(value):
                    self.categorized_data["birthday"].append(value)
                elif email_regex.match(value):
                    self.categorized_data["email"].append(value)
                else:
                    formatted_name = self.format_name(value)
                    if formatted_name is not None:
                        self.categorized_data["name"].append(formatted_name)


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