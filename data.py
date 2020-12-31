import pandas
from sample import *

# this class creat an object to store the data.
class Data:
    def __init__(self, path):
        df = pandas.read_csv(path)
        self.data = df.values.tolist()

# this function returns a list of objects of type Sample.

    def create_samples(self):
        samples_list = []
        for line in self.data:
            txt = line[0]
            s_id = int(txt.partition("_")[-1])
            label = line[-1]
            line.pop(0)
            line.pop(-1)
            genes = line
            samples_list.append(Sample(label, genes, s_id))
        return samples_list









