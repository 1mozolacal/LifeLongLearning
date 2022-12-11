import pandas as pd
from scipy.cluster import hierarchy

# Load the data
data = pd.read_csv(r'C:\Users\elugez\Dropbox\Ryerson\Teaching\CPS844\Elodie\Chap7\Demo\vertebrate.csv')

# Drop the class labels and keep the numerical attributes
X = data.drop(['Name', 'Class'], axis=1)

# Hierarchical agglomerative clustering - average method
Z = hierarchy.average(X)

# Plot the dendrogram
dn = hierarchy.dendrogram(Z, labels = data['Name'].to_list())

# For 5 clusters from the data, such that no more than 5 clusters
# are created, but that, at the same time, the distance between the last 
# merged clusters is minimized
k = 5
cLabels = hierarchy.fcluster(Z, k, criterion = 'maxclust')

# Concatenate the dataframe 'data' with the array of labels
data = pd.concat((data, pd.DataFrame(cLabels, columns = ['Labels'])), axis=1)