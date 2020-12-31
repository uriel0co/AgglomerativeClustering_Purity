

# the class computes distances between two given clusters using different matrix(single/complete).
class Link:

    # Raises an exception if the abstract method "compute" does not get implemented
    def compute(self, cluster, other, distances=None):
        raise NotImplementedError("Subclass must implement abstract method")


class SingleLink(Link):
    # create a list of euclidean distances of each point of 1 cluster to each point in the other cluster.
    # and returns the min distance.
    # Overrides method in Link class.
    # Parameters: matrix - The distances matrix.
    # cluster, other - two clusters getting computed.
    # Returns: min_distance - the distance computed by Single Link metric.
    def compute(self,  matrix, cluster, other):
        min_distance = matrix[cluster.samples[0].s_id][other.samples[0].s_id]
        for s2 in other.samples:
            for s1 in cluster.samples:
                new_distance = matrix[s1.s_id][s2.s_id]
                if new_distance < min_distance:
                    min_distance = new_distance
        return min_distance


class CompleteLink(Link):
    # creat a list of euclidean distances of each point of 1 cluster to each point in the other cluster.
    # and returns the max distance.
    # Overrides method in Link class.
    # Parameters: matrix - The distances matrix.
    # cluster, other - two clusters getting computed.
    # Returns: max_distance - the distance computed by Complete Link metric.
    def compute(self,  matrix, cluster, other):
        max_distance = matrix[cluster.samples[0].s_id][other.samples[0].s_id]
        for s1 in cluster.samples:
            for s2 in other.samples:
                new_distance = matrix[s1.s_id][s2.s_id]
                if new_distance > max_distance:
                    max_distance = new_distance
        return max_distance