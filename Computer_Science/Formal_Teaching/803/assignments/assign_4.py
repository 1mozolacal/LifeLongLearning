import pandas as pd
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN, KMeans
from sklearn.model_selection import GridSearchCV
import math
import csv

# Load the data
raw_data = pd.read_csv('dataset.csv')
pre_shape = raw_data.shape


# ============================
#     Explore The Data
# ============================

print(f"Raw data rows {pre_shape[0]} with {pre_shape[1]} attributes")

# Explore the countries/countriesCode attribute
amount_of_countries = len(raw_data.countryCode.unique())
print(f"Number of countries {amount_of_countries} can be "
      + f"represented with {math.ceil(math.log(amount_of_countries,2))} bits")
keep_country_thresh = 100
country_list = [[len(raw_data[raw_data.countryCode == country]), country]
                for country in raw_data.countryCode.unique()]
country_list.sort(key=lambda a: a[0], reverse=True)
keeping_country = [x[0] for x in country_list if x[0] >= keep_country_thresh]
discard_country = [x[0] for x in country_list if x[0] < keep_country_thresh]
print(f"Keeping {len(keeping_country)} with population of {sum(keeping_country)}"
      + f"\nDiscarding {len(discard_country)} with population of {sum(discard_country)}"
      + f"\nRemoving {round(len(discard_country)/(len(discard_country)+len(keeping_country)),2)}% but keeping {round(sum(keeping_country)/(sum(keeping_country)+sum(discard_country)),2)}% population")

# ============================
#    Preprocessing Steps
# ============================

# Drop all rows with any null data
no_null = raw_data[~raw_data.isnull().any(axis=1)]

# Drop columns that are not necessary
dropped_columns = no_null.drop(columns=['identifierHash', 'type', 'hasAnyApp',
                                        'seniorityAsMonths', 'seniorityAsYears', 'civilityTitle', 'gender', 'country'])

# Convert Gender to 0 or 1
gender_standarization = dropped_columns
gender_standarization['civilityGenderId'] = gender_standarization['civilityGenderId'].apply(
    lambda x: min(x-1, 1))

# Reduce the number of countries
country_count = raw_data.countryCode.value_counts()
countries_keeping_names = [x for x in raw_data.countryCode.unique(
) if x in country_count and country_count[x] >= keep_country_thresh]

country_prune = gender_standarization[gender_standarization['countryCode'].isin(
    countries_keeping_names)]

print(f"TEST {len(country_prune)} - {len(country_prune.countryCode.unique())}")

# Binary decodeing for country and language
binary_decoding = pd.get_dummies(country_prune,
                                 columns=['countryCode', 'language'],
                                 prefix=['country', 'language'])

# Finsished preprocessing
preprocessed_data = binary_decoding


# ============================
#    Trainging the Model
# ============================

print("training model...")


parameters = {'n_clusters': [x for x in range(2, 8)]}
clf = GridSearchCV(KMeans(random_state=0), parameters)
clf.fit(preprocessed_data)

model = clf.best_estimator_
print("The number of clusters should be", clf.best_params_)


# Write all cluster to an output file
with open('calvinMozola_out.csv', 'w', newline='') as outFile:

    spamwriter = csv.writer(outFile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(preprocessed_data.columns)
    for cluster in model.cluster_centers_:
        spamwriter.writerow(([str(x) for x in cluster]))


print("Finished!")
