from pathlib import Path
from datetime import datetime
from re import compile

from utils.validate_regex import is_valid_regex
from utils.format_name import format_name

class Classify:
    def __init__(self, dir: Path):
        self.dir = dir
        self.raw_data = [] # array of sets
        self.aggregated_raw_data = set()
        self.redundant_data = {}
        self.categorized_data = None

        # checks if the path exists before reading data sets
        if(dir.is_dir()):
            self.__read_data_sets()
            self.__aggregate_raw_data()
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

    def __aggregate_raw_data(self):
        for data_set in self.raw_data:
            self.aggregated_raw_data.update(data_set)

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

        init_categorized_data = { # dictionary of sets for categorize_data
            "name": set(),
            "birthday": set(),
            "email": set(),
            "cell_no": set(),
        }

        # Regex for cell numbers, birthdays, and emails
        cell_no_regex = compile(r'^\+63-\d{10}$')
        birthday_regex = compile(r'^\d{4}-\d{2}-\d{2}$')
        email_regex = compile(r'^.+@.+\..{2,}$')
        
        for data_set in self.raw_data:
            for value in data_set:
                if cell_no_regex.match(value):
                    init_categorized_data["cell_no"].add(value)
                elif birthday_regex.match(value):
                    init_categorized_data["birthday"].add(value)
                elif email_regex.match(value):
                    init_categorized_data["email"].add(value)
                else:
                    formatted_name = format_name(value)
                    init_categorized_data["name"].add(formatted_name)

        self.categorized_data = init_categorized_data
        return self
    
    def categorize_data_by(self, patterns: dict):
        """
        Categorize the raw data based on user input category and regex
        """
        # initialize a categorized data dictionary
        init_categorized_data = { key:set() for key in patterns if is_valid_regex(patterns[key]) }
        
        # loop through the aggregated raw data
        for value in self.aggregated_raw_data:
            # loop through the keys and check if any of them are a match
            for key in init_categorized_data:
                if compile(patterns[key]).match(value):
                    init_categorized_data[key].add(value)

        self.categorized_data = init_categorized_data
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
        print(f"\n-----categorized_data-----")
        # self.categorize_data()

        if self.categorized_data is not None:
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
        if self.categorized_data is None:
            return self
        
        # get current datetime for filename and writing timestamp on DATABASE_current_datetime.txt
        current_datetime = datetime.now()
        text_file_path = self.dir / 'categorized_database' / f'DATABASE_{current_datetime.strftime(r"%Y%m%d_%H%M%S%f")}.txt'
        
        # create text file from path
        Path.mkdir(text_file_path.parent, exist_ok=True)

        # open text file and write to file
        with open(text_file_path, 'w') as file:
            file.write(f'DATABASE (created on {current_datetime.strftime(r"%Y-%m-%d %H:%M:%S")})\n')

            # get total data
            total_data = sum(len(dataset) for dataset in self.categorized_data.values())
            file.write(f'Total data: {total_data}\n\n')

            for category, dataset in self.categorized_data.items():
                file.write(f"{category} ({len(dataset)} total):\n")
                
                for data in dataset:
                    file.write(f"\t{data}\n")
                
                file.write('\n')