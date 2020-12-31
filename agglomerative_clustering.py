from cluster import *


# The class runs the clustering algorithm.
class AgglomerativeClustering:
    def __init__(self, samples, link):
        self.samples = samples
        self.link = link

    # The method find the two closest clusters.
    # Parameters: matrix - The distances matrix, clusters_List - dynamic list of clusters.
    # Returns: [c1, c2] - list of the two closest clusters.
    def closest_clusters(self, matrix, clusters_list):
        min_distance = self.link.compute(matrix, clusters_list[1], clusters_list[0])
        c1 = 0
        c2 = 1
        for cluster1 in range(len(clusters_list)):
            for cluster2 in range(cluster1 + 1, len(clusters_list)):
                new_distance = self.link.compute(matrix, clusters_list[cluster2], clusters_list[cluster1])
                if min_distance > new_distance:
                    c1 = cluster1
                    c2 = cluster2
                    min_distance = new_distance
        return [c1, c2]

    # The method runs the algorithm.
    # Creates a distance matrix, creates an initial clusters for each sample.
    # maintains a list of clusters.
    # Implementing the merge method, merging two relevant clusters, while pop out one of the two merged classes.
    # Calling __str__ method in Cluster class for printing.
    # (the one with the bigger index)
    # Parameters: max_clusters - limit of wanted clusters, the algorithms will stop when reaching this limit.
    def run(self, max_clusters):
        len_samples = len(self.samples)
        clusters_list = []
        matrix = [[0 for x in range(len_samples)] for y in range(len_samples)]
        for i in range(len_samples):
            cluster = Cluster([self.samples[i]], i)
            clusters_list.append(cluster)
            sample1 = self.samples[i]
            for j in range(i + 1, len_samples):
                sample2 = self.samples[j]
                matrix[j][i] = sample1.compute_euclidean_distance(sample2)
                matrix[i][j] = matrix[j][i]
                num_of_clusters = len(clusters_list)
        while num_of_clusters > max_clusters:
            c1_and_c2 = self.closest_clusters(matrix, clusters_list)
            c1 = c1_and_c2[0]
            c2 = c1_and_c2[1]
            clusters_list[c1].merge(clusters_list[c2])
            clusters_list.pop(c2)
            num_of_clusters = len(clusters_list)
        for final_cluster in clusters_list:
            final_cluster.__str__()










