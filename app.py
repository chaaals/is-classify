from pathlib import Path
from algorithm.classify import Classify

if __name__ == '__main__':
    DATA_DIR = Path(__file__).parent / 'data'
    classify = Classify(DATA_DIR)
    classify.print_categorized_data()
    classify.export_categorized_data()
