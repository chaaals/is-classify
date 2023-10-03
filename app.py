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
    # Buo ang output file path na DATABASE.txt
    output_file_path = Path(__file__).parent / 'data' / 'categorized_database' / 'DATABASE.txt'

    with open(output_file_path, 'w') as f:
        # Isulat ang petsa at oras sa header ng DATABASE
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"DATABASE (created on {formatted_datetime})\n")

        for category, dataset in classify.get_categorized_data().items():
            # Isulat ang kategorya
            f.write(f"{category}:\n")

            # Isulat ang dataset
            for data in dataset:
                f.write(f"\t{data}\n")
            
            # Magdagdag ng newline pagkatapos ng dataset
            f.write('\n')

if __name__ == '__main__':
    DATA_DIR = Path(__file__).parent / 'data'
    classify = Classify(DATA_DIR)

    print_to_terminal(classify)
    write_to_file(classify)
