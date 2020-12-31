# this class creat cluster objects that contain their id and a list of samples.
class Cluster:
    def __init__(self, samples, c_id):
        self.samples = samples
        self.c_id = c_id

# this function merge two clusters by adding one sample list to the other.
    def merge(self, other):
        self.c_id = min(self.c_id, other.c_id)
        self.samples += other.samples

# this function returns the purity of a cluster and the dominant label of the samples in it.
    def compute_purity(self):
        label_order = {}
        correct_labels = 0
        for sample in self.samples:
            label_order[sample.label] = 0
        for sample in self.samples:
            label_order[sample.label] += 1
        sum_of_samples = len(self.samples)
        dominant_label = self.find_dominanat(label_order)
        for sample in self.samples:
            if sample.label == dominant_label:
                correct_labels += 1
        purity = correct_labels/sum_of_samples
        return [purity, dominant_label]

#  this function returns the key that its value is the greatest.
# Parameters:
#       label_order - a dictionary in which the key represents a label and the value of a key is the frequency of
#       that label in a cluster.
#       max_key - the most dominant label in a cluster.
    def find_dominanat(self, label_order):
        max_label = label_order[[*label_order][0]]
        max_key = [*label_order][0]
        for key in label_order:
            if label_order[key] > max_label:
                max_label = label_order[key]
                max_key = key
        return max_key

# this function prints for each cluster its id, the samples in it, its dominant label, and its purity.
    def __str__(self):
        result = self.compute_purity()
        purity = result[0]
        dominant_label = result[1]
        list_id = [one_sample.s_id for one_sample in self.samples]
        print("Cluster {}: {}, dominant label: {}, purity: {}".format(self.c_id, sorted(list_id),
                                                                      dominant_label, purity))











