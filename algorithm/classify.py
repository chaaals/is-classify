from pathlib import Path
from datetime import datetime
import re
from utils.format_name import format_name

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
                if cell_no_regex.match(value):
                    self.categorized_data["cell_no"].add(value)
                elif birthday_regex.match(value):
                    self.categorized_data["birthday"].add(value)
                elif email_regex.match(value):
                    self.categorized_data["email"].add(value)
                else:
                    formatted_name = format_name(value)
                    self.categorized_data["name"].add(formatted_name)

        return self
    
    def get_categorized_data(self) -> dict[str:set]:
        """
        Getter function for categorized data
        """
        return self.categorized_data
    
    def print_categorized_data(self):
        """
        Print categorized data to the terminal
        """
        # print raw data by file
        for i, dataset in enumerate(self.get_raw_data()):
            print(f"--------file_{i+1}--------")
            print(f"{dataset}\n")

        # print found redundant data
        print(f"------redundant_data------")
        for data, times_repeated in self.get_redundant_data().items():
            print(f"'{data}' was repeated {times_repeated} time", end='')

            # 1 time, 2 times, 3 times, ..., n times
            if times_repeated > 1:
                print("s")

        # print categorized data
        print(f"-----categorized_data-----")
        self.categorize_data()

        for category, dataset in self.get_categorized_data().items():
            print(f"{category}:")
            print(dataset)
            print('\n')

        return self

    def export_categorized_data(self):
        """
        write the categorized database to a text file
        the export path will always be a text file under "categorized_database" directory in the same directory as the data_set files

        data/
        |___ data_set.txt files...
        |___ categorized_database/
            |___DATABASE.txt
        """
        text_file_path = self.dir / 'categorized_database' / f'DATABASE.txt'
        # create text file from path
        Path.mkdir(text_file_path.parent, exist_ok=True)

        # open text file and write to file
        with open(text_file_path, 'w') as database:
            current_datetime = datetime.now().strftime(r'%Y-%m-%d %H:%M:%S')
            database.write(f'DATABASE (created on {current_datetime})\n')

            # get total data
            total_data = sum(len(dataset) for dataset in self.categorized_data.values())
            database.write(f'Total data: {total_data}\n\n')

            for category, dataset in self.categorized_data.items():
                database.write(f"{category} ({len(dataset)} total):\n")
                
                for data in dataset:
                    database.write(f"\t{data}\n")
                
                database.write('\n')