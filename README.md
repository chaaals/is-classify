# IS Lab activity 2

Classification Algorithm

#### Developed by

- Masapol, Cid (Leader)
- Benevides, Sean Lester
- Ching, Charles Matthew
- Palileo, Jethro
- Sundiam, Eidrian
- Villanueva, Andre

## Features

Classify is an algorithm that categorizes raw data from data sets. Currently, it supports categorization of `name`, `birthday`, `email`, and `cell_no`.

To get started, create an instance of Classify:

```py
from algorithm.classify import Classify

c = Classify('< your data set directory >')
```

#### Methods

By creating an instance of the Classify algorithm, it exposes these following methods to the user:

- `c.get_raw_data()` -> Gets the raw data
- `c.get_aggregated_data()` -> Gets the aggregated raw data
- `c.get_unmatched_data()` -> Gets the unmatched data on after categorization
- `c.get_redundant_data()` -> Gets the redundant data
- `c.get_categorized_data()` -> Gets the categorized data
- `c.print_categorized_data()` -> Prints the categorized data
- `c.categorize_data()` -> Categorizes the raw data
- `c.export()` -> Exports the categorized data in a `.txt` file

## Instructions

1. Clone the repository.
2. Create a virtual environment. `python -m venv .env`
3. Activate your virtual environment `./.env/Scripts/activate.bat`
4. Install dependencies `python -m pip install -r requirements.txt`
5. To run unit tests, use this command `python -m unittest -v test.test_classify`
6. To generate data, use this command `python generate_dataset.py --length 25 --count 5`

Note: Don't forget to deactive your virtual environment afterwards.
