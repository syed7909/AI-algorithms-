import numpy as np
import math
import pandas as pd




class K_Means:

    def __init__(self, k =3, tolerance = 0.0001, max_iterations = 500):
        self.k = k
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        
df = pd.read_csv(r"/Users/hasanaskary/Downloads/fruitsd.csv")

df = df[['one', 'two']]
dataset = df.astype(float).values.tolist()

X = df.values

def Euclidean_distance(feat_one, feat_two):

    squared_distance = 0

    

    for i in range(len(feat_one)):

            squared_distance += (feat_one[i] – feat_two[i])**2

    ed = sqrt(squared_distances)

    return ed;

for i in range(self.k):
    self.centroids[i] = data[i]
    
for i in range(self.max_iterations):
        self.classes = {}
        for i in range(self.k):
            self.classes[i] = []


        for features in data:
            distances = [np.linalg.norm(features - self.centroids[centroid]) for centroid in self.centroids]
            classification = distances.index(min(distances))
            self.classes[classification].append(features)
previous = dict(self.centroids)


for classification in self.classes:
    self.centroids[classification] = np.average(self.classes[classification], axis = 0)
    
isOptimal = True #to check the optimal no of centroids......

for centroid in self.centroids:

    original_centroid = previous[centroid]
    curr = self.centroids[centroid]

    if np.sum((curr - original_centroid)/original_centroid * 100.0) > self.tolerance:
        isOptimal = False


if isOptimal:
        break

