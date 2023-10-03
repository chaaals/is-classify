from pathlib import Path
from algorithm.classify import Classify

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

"def write_to_file(classify: Classify):
 "   pass

"if __name__ == '__main__':
 "   DATA_DIR = Path(__file__).parent / 'data'
  "  classify = Classify(DATA_DIR)

   " print_to_terminal(classify)
    "write_to_file(classify)

def write_to_file(classify: Classify):
    output_file_path = Path(__file__).parent / 'output.txt'  # Output file path in the same directory as the script
    with open(output_file_path, 'w') as output_file:
        for category, data_set in print_to_txt.items():
            output_file.write(f"{category}\n")
            for data in data_set:
                output_file.write(f"     {data}\n")

if __name__ == '__main__':
    DATA_DIR = Path(__file__).parent / 'data'
    classify = Classify(DATA_DIR)

    print_to_terminal(classify)
    write_to_file(classify)
