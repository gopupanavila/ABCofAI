import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommendations(data_file, appliance_type, preferences=None):
    # read the dataset
    df = pd.read_csv(data_file)
    # df = df[df.appliance_type == appliance_type]

    # helper function for retrieving items based on index
    def get_items_from_index(index):
        try:
            index_df = df.iloc[index]
            return zip(index_df["items"].split(','),
                       index_df["quantities"].split(','))
        except Exception:
            print(f'No zipped data available at this {index}')
            return

    # helper function for retrieving index of
    # one of the high rated purchases
    def get_index(rating, appliance_type, preferences):
        filtered_frame = df[(df['rating'] >= rating) & (df['appliance_type'] == appliance_type)]
        if preferences:
            for pref in preferences:
                filtered_frame = filtered_frame[filtered_frame['items'].str.contains(pref)]
        return filtered_frame.index[0]

    # helper function to combine the features
    def combine_features(row):
        try:
            return row['appliance_type'] + ' ' + ' '.join(row['items'].split(',')) + ' ' + str(row['rating'])
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

    app_index = get_index(10, appliance_type, preferences)
    similar_appliances = list(enumerate(cosine_sim[app_index]))
    sorted_similar_appliances = sorted(similar_appliances,
                                       key=lambda x: x[1],
                                       reverse=True)
    result = set()
    for element in sorted_similar_appliances[:10]:
        _res = get_items_from_index(element[0])
        if _res:
            result.add(_res)

    return list(result)


if __name__ == '__main__':
    import sys
    print(recommendations(sys.argv[1], sys.argv[2]))
