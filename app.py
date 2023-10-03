from pathlib import Path
from algorithm.classify import Classify

def main():
    DATA_DIR = Path(__file__).parent / 'data'
    
    classify = Classify(DATA_DIR)

    # print raw data by file
    for i, dataset in enumerate(classify.get_raw_data()):
        print(f"--------file_{i+1}--------")
        print(f"{dataset}\n")

    # print found redundant data
    print(f"------redundant_data------")
    print(f"{classify.get_redundant_data()=}\n")

    # print categorized data
    print(f"-----categorized_data-----")
    classify.categorize_data()

    for category, dataset in classify.get_categorized_data().items():
        print(f"{category}:", end = "\n\t")
        for data in dataset:
            print(data, end='\n\t')
        print('\n')

if __name__ == '__main__':
    main()