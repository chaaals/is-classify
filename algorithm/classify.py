from pathlib import Path
from datetime import datetime

from warnings import warn
from constants.user_info import UserInfo
from utils.format_name import format_name

class Classify:
    def __init__(self, dir: Path):
        self.dir = dir
        self.raw_data = [] # array of sets
        self.aggregated_raw_data = set()

        self.redundant_data = {}
        self.unmatched_data = set()
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
        """
        Aggregates raw data to a set
        """
        for data in self.raw_data:
            self.aggregated_raw_data.update(data)
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
        
        init_categorized_data = {
            "name": set(),
            "birthday": set(),
            "email": set(),
            "cell_no": set(),
        }

        for data in self.aggregated_raw_data:
            if UserInfo.CELL_NO_REGEXP.match(data):
                init_categorized_data['cell_no'].add(data)
            elif UserInfo.BIRTHDAY_REGEXP.match(data) and UserInfo.is_valid_birthday(data):
                init_categorized_data['birthday'].add(data)
            elif UserInfo.EMAIL_REGEXP.match(data):
                init_categorized_data['email'].add(data)
            elif UserInfo.NAME_REGEXP.match(data):
                formatted_name = format_name(data)
                init_categorized_data['name'].add(formatted_name)
            else:
                self.unmatched_data.add(data)
        
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
        if self.categorized_data is not None:
            print(f"-----categorized_data-----")

            for category, dataset in self.get_categorized_data().items():
                print(f"{category}:")
                print(dataset)
                print('\n')

        return self

    def export(self):
        """
        write the categorized database to a text file
        the export path will always be a text file under "categorized_database" directory in the same directory as the data_set files

        data/
        |___ data_set.txt files...
        |___ categorized_database/
            |___DATABASE.txt
        """
        if self.categorize_data is None:
            warn(f'Cannot export categorized_data typeof {type(self.categorized_data)}. Call categorize_data() method first.')
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