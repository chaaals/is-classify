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
        print('\n'.join(dataset))  # Add a newline after each data point
        print('\n')

def write_to_file(classify: Classify):
    output_dir = Path(__file__).parent / 'data' / 'categorized_database'
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file_path = output_dir / 'DATABASE.txt'  # Output file path named DATABASE.txt
    with open(output_file_path, 'w') as output_file:
        print_to_txt = classify.get_categorized_data()
        for category, data_set in print_to_txt.items():
            output_file.write(f"{category} ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}): {len(data_set)}\n")
            for data in data_set:
                output_file.write(f"\t{data}\n")  # Use '\t' instead of spaces

if __name__ == '__main__':
    DATA_DIR = Path(__file__).parent / 'data'
    classify = Classify(DATA_DIR)

    print_to_terminal(classify)
    write_to_file(classify)
