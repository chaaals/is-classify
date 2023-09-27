import os
from algorithm.classify import Classify


if __name__ == '__main__':
    DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

    classify = Classify(DATA_DIR)
    print(*classify.get_raw_data(), sep='\n\n')
    print(classify.get_redundant_data())