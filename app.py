from pathlib import Path
from algorithm.classify import Classify

if __name__ == '__main__':
    DATA_DIR = Path(__file__).parent / 'data'
    classify = Classify(DATA_DIR)

    # classify.categorize_data_by({
    #     "full_name": r'^[A-Z][a-zA-Z]*(?:\s[A-Z][a-zA-Z]*){1,2}$',
    #     "cell_number": r'^\+63-\d{10}$',
    #     "birthday": r'^\d{4}-\d{2}-\d{2}$',
    #     "email": r'^.+@.+\..{2,}$',
    # }).export()

    classify.categorize_data().export()

    classify.print_categorized_data()
