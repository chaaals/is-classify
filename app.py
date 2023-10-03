from pathlib import Path
from algorithm.classify import Classify
from datetime import datetime

def print_to_terminal(classify: Classify):
    # print raw data by file
    for i, dataset in enumerate(classify.get_raw_data()):
        print(f"--------file_{i+1}--------")
        print(f"{dataset}\n")

    # print found redundant data
    print(f"------redundant_data------")
    for data, times_repeated in classify.get_redundant_data().items():
        print(f"'{data}' was repeated {times_repeated} time", end='')

        # 1 time, 2 times, 3 times, ..., n times
        if times_repeated > 1:
            print("s")

    # print categorized data
    print(f"-----categorized_data-----")
    classify.categorize_data()

    for category, dataset in classify.get_categorized_data().items():
        print(f"{category}:")
        print(dataset)
        print('\n')

def write_to_file(classify: Classify):
    # get categorized data
    categorized_data = classify.get_categorized_data()

    # create text file from path
    text_file_path = Path(__file__).parent / 'data' / 'categorized_database' / f'DATABASE.txt'
    Path.mkdir(text_file_path.parent, exist_ok=True)

    # open text file and write to file
    with open(text_file_path, 'w') as database:
        current_datetime = datetime.now().strftime(r'%Y-%m-%d %H:%M:%S')
        database.write(f'DATABASE (created on {current_datetime})\n')

        # get total data
        total_data = sum(len(dataset) for dataset in categorized_data.values())
        database.write(f'Total data: {total_data}\n\n')

        for category, dataset in categorized_data.items():
            database.write(f"{category} ({len(dataset)} total):\n")
            
            for data in dataset:
                database.write(f"\t{data}\n")
            
            database.write('\n')

if __name__ == '__main__':
    DATA_DIR = Path(__file__).parent / 'data'
    classify = Classify(DATA_DIR)

    print_to_terminal(classify)
    write_to_file(classify)
