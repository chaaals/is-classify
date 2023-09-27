from faker import Faker
import random

fake = Faker()

def generate_dataset(length: int):
    file_name = f'./data/data_set_{random.randint(1,5000)}.txt'

    with open(file_name, 'w') as file:
        for j in range(length):
            rand = random.randint(1,100)

            if(rand >= 1 and rand <=25):
                file.write(fake.name() + '\n')
                continue

            if(rand >= 26 and rand <= 50):
                file.write(fake.email() + '\n')
                continue

            if(rand >= 51 and rand <= 75):
                file.write(fake.date() + '\n')
                continue

            if(rand >= 76 and rand <= 100):
                file.write(f"+63-9{fake.msisdn()[4:]}" + '\n')
                continue
                

generate_dataset(25)