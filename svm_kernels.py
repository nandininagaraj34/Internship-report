import sys
sys.path.append("..")
from src.svdd import SVDD
from src.visualize import Visualization as draw
from data import PrepareData as load
from sklearn.cluster import KMeans

# load data
trainData, testData, trainLabel, testLabel = load.banana()


# kernel list
kernelList = {"1": {"type": 'gauss', "width": 1/24},
              "2": {"type": 'linear', "offset": 0},
              "3": {"type": 'ploy', "degree": 2, "offset": 0},
              "4": {"type": 'tanh', "gamma": 1e-4, "offset": 0},
              "5": {"type": 'lapl', "width": 1/12}
              }


for i in range(len(kernelList)):

    # set SVM parameters
    parameters = {"positive penalty": 0.9,
                  "negative penalty": 0.8,
                  "kernel": kernelList.get(str(i+1)),
                  "option": {"display": 'on'}}
    
    # construct an SVM model
    svdd = SVDD(parameters)
    
    # train SVM model
    svdd.train(trainData, trainLabel)
      
    # test SVM model
    distance, accuracy = svdd.test(testData, testLabel)
    
    # visualize the results
    # draw.testResult(svm, distance)
    # draw.testROC(testLabel, distance)
    draw.boundary(svdd, trainData, trainLabel)

# Kmeans Clustering
def train_k_means_clustering(data, k, epochs):
    dims = len(data[0])
    print('data[0]:',data[0])
    centers = random_centers(dims,k)

    clustered_data = point_clustering(data, centers, dims, first_cluster=True)

    for i in range(epochs):
        centers = mean_center(clustered_data, centers, dims)
        clustered_data = point_clustering(data, centers, dims, first_cluster=False)

    return centers

def compute_euclidean_distance(point, centroid):
    return np.sqrt(np.sum((point - centroid)**2))

