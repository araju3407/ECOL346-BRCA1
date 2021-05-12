# ECOL346 S21 BRCA1 Project

"""This script shows how clustering methods were utilized in this project.
"""

import pandas as pd
import matplotlib.pyplot as plt

from sklearn import decomposition
from sklearn.cluster import KMeans

# Import dataset containing gene expression matrix
x=pd.read_csv("expression.csv")
del x["Unnamed: 0"]
del x["ID_REF"]
print(x)

# PCA
pca, X_pca = None, None
for i in range(2,31):
    pca = decomposition.PCA(n_components=i)
    pca.fit(x)
    X_pca = pca.transform(x)
    print(pca.explained_variance_ratio_)
    print(pca.components_)

# Kmeans
kmeans = KMeans(n_clusters=2)
kmeans.fit(x)

print(kmeans.labels_)
print(kmeans.cluster_centers_)

plt.figure()
plt.scatter(X_pca[:,0], X_pca[:, 1], c = kmeans.labels_, cmap='rainbow', alpha=0.5)
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:, 1], color="black")
plt.savefig("kmeans.png")
