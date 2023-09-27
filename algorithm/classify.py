import os

class Classify:
    def __init__(self,dir: str):
        self.dir = dir
        self.raw_data = []

        # checks if the path exists before reading data sets
        if(os.path.exists(dir)):
            self.read_data_sets()
        else:
            raise ValueError('Argument must be a valid directory.')

    def read_data_sets(self):
        """
        Read the files and in a given dir and stores the value in a 2D array
        """ 
        files = os.listdir(self.dir)
        
        for file in files:
            path = os.path.join(self.dir, file)
            file_data = []
            
            with open(path, 'r') as f:
                for line in f:
                    file_data.append(line.strip())

            self.raw_data.append(file_data)

        return self
    
    def get_raw_data(self) -> list:
        """
        Getter fn for raw data
        """
        return self.raw_data
