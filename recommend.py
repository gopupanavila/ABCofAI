import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommendations(data_file, appliance_type):
    # read the dataset
    df = pd.read_csv(data_file)

    # helper function for retrieving items based on index
    def get_items_from_index(index):
        return df[df.index == index]["items"].values[0]

    # helper function for retrieving index based on appliance type
    def get_index_from_appliance_type(app_type):
        app_types = df[df.appliance_type == app_type]
        return app_types[app_types.rating > 5]["index"].values[0]

    # helper function to combine the features
    def combine_features(row):
        try:
            return row['appliance_type'] + " " + ' '.join(row['items'].split(',')) + ' ' + str(row['rating'])
        except:
            print("Error:", row)

    features = ['appliance_type', 'items', 'rating']
    for feature in features:
        df[feature] = df[feature].fillna('')  # fill all NaN

    df["combined_features"] = df.apply(combine_features, axis=1)

    # for feature extraction
    # https://www.educative.io/edpresso/countvectorizer-in-python
    cv = CountVectorizer()

    # The fit method is calculating the mean and variance of each of
    # the features present in our data. The transform method is transforming
    # all the features using the respective mean and variance.
    count_matrix = cv.fit_transform(df["combined_features"])

    # Cosine similarity is a metric used to determine how similar
    # the documents are irrespective of their size
    cosine_sim = cosine_similarity(count_matrix)

    app_index = get_index_from_appliance_type(appliance_type)
    similar_appliances = list(enumerate(cosine_sim[app_index]))
    reverse_it = appliance_type.lower() == 'office'
    sorted_similar_appliances = sorted(similar_appliances,
                                       key=lambda x: x[1],
                                       reverse=reverse_it)
    result = []
    for element in sorted_similar_appliances[:5]:
        result.append(get_items_from_index(element[0]))
    return result


if __name__ == '__main__':
    import sys
    print(recommendations(sys.argv[1], sys.argv[2]))
