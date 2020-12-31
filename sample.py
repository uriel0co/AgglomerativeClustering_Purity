# this class creat sample objects that contain for each sample its i.d, label and a list of genes.
class Sample:
    def __init__(self, label, genes, s_id):
        self.s_id = s_id
        self.genes = genes
        self.label = label

# this function returns the calculation of the euclidean_distance between two given samples, using their list of genes.
    def compute_euclidean_distance(self, other):
        return (sum((my - his)**2 for my, his in zip(self.genes, other.genes)))**0.5

