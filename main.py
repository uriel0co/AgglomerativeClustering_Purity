import sys
from agglomerative_clustering import *
from data import *
from link import *


def main(argv):
    data1 = Data(argv[1])
    samples_list = data1.create_samples()
    links = argv[2].replace("_", " ")
    links = links.split(", ")
    print(links[0] + ":")
    single_link = SingleLink()
    agglomerative = AgglomerativeClustering(samples_list, single_link)
    agglomerative.run(int(argv[3]))
    print()
    print()
    print(links[1] + ":")
    complete_link = CompleteLink()
    agglomerative = AgglomerativeClustering(samples_list, complete_link)
    agglomerative.run(int(argv[3]))



if __name__ == "__main__":
    main(sys.argv)
