import pandas as pd
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA

# Import the data
data = pd.read_table('data.txt')

# Data preparation
# Check the data size
shape_before = data.shape

# Drop records with any missing entries
data.dropna(inplace=True)

# Check the data size after dropping records with missing entries
data.shape

# Drop records when participants age is > 80
data=data[data['age'] <= 80]

# Check entered country codes
data.country.unique()

# Remove records with wrong country code
data= data[data.country != '(nu']

# Check entered engnat values
data.engnat.unique()

# Remove missing values (0 values)
data=data[data.engnat != 0]

# Repeat process
data.race.unique()
data=data[data.race != 0]
data=data[data.gender != 0]
data=data[data.hand != 0]

# Check the data size now
shape_now = data.shape

# Data reduction
X = data.iloc[:, 7:].values

# Standardize the data
X = scale(X)

# PCA analysis
pca5 = PCA(n_components=5)
#Fit a probabilistic PCA model with X and apply the dimensionality reduction on X. 
reducedData = pca5.fit_transform(X)

# Consolidate the data
reducedData = pd.DataFrame(reducedData, columns = ['principal component 1', 'principal component 2', 'principal component 3', 'principal component 4', 'principal component 5'])

# Finish consolidating the data
reducedData = pd.concat([data.iloc[:, 0:7].reset_index(drop=True) , reducedData.reset_index(drop=True)], axis = 1)

# Check the size of the dataset now
shape_now = reducedData.shape

# Transform country feature 
X = data.iloc[:, 6]
X = pd.get_dummies(X, prefix = "Co")

# Consolidate the data
reducedData=pd.concat([reducedData.iloc[:, 0:6].reset_index(drop=True) , X.reset_index(drop=True), reducedData.iloc[:, 7:].reset_index(drop=True)], axis = 1)
