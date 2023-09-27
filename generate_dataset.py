from faker import Faker
from random import randint

# read command line args
from sys import argv

def generate_dataset(fake: Faker, length: int = 25) -> None:
    """
    generate dataset composed of name, email, date, and phone number based on length passed
    """
    file_name = f'./data/data_set_{randint(1,5000)}.txt'

    with open(file_name, 'w') as file:
        for j in range(length):
            rand = randint(1,4)

            if(rand == 1):
                file.write(f"{fake.first_name()} {fake.last_name_female()} {fake.last_name_male()}\n")

            elif(rand == 2):
                file.write(f"{fake.email()}\n")

            elif(rand == 3):
                file.write(f"{fake.date()}\n")

            elif(rand == 4):
                file.write(f"+63-9{fake.msisdn()[4:]}\n")

def parse_args(argv: list[str] = None) -> tuple[int, int]:
    """
    length is the number of data in a dataset
    count is the number of datasets to be generated
    return: (length, count) or None if there are no args
    valid arguments: --length, -l, --count, -c
    """
    # create default 1 containers for length and value
    length = 1
    count = 1
    
    # check if list
    if not isinstance(argv, list):
        raise TypeError("Please pass list of arguments (strings)")
    # check if list of strings
    if not all(isinstance(arg, str) for arg in argv):
        raise TypeError("Please pass list of arguments (all must be strings)")        
    
    # create iter object for the for loop
    # so we can use next() which can get the value of the next iteration
    argv_iter = iter(argv)

    for arg in argv_iter:
        # put None as default value if there's no next iteration
        value = next(argv_iter, None)

        # check if value is digit before proceeding
        # (also to not write "and value.isdigit()" in every if)
        if value.isdigit():
            if arg in ["--length", "-l"]:
                length = int(value)
            
            elif arg in ["--count", "-c"]:
                count = int(value)

    return length, count


# python convention to differentiante runnable scripts with libraries
if __name__ == "__main__":
    int_list = [1,2,3,4]
    # don't include the first argument which is always the script's filename
    length, count = parse_args(argv[1:])

    fake = Faker()
    for _ in range(count):
        generate_dataset(fake, length)
