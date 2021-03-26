import pandas as pd

# Pandas dataframe exercises
# simple dataframe
# data = {
#     'apples': [3, 2, 0, 1],
#     'oranges': [0, 3, 7, 2]
# }
# purchases = pd.DataFrame(data)
# print(purchases)

# load data from csv file
# df = pd.read_csv('appliances_rating.csv') #, index_col=0)
# print(df)
# print(df.loc[2])
# print(df.set_index('no'))

# convert to csv
# data = {
#     'apples': [3, 2, 0, 1],
#     'oranges': [0, 3, 7, 2]
# }
# df = pd.DataFrame(data)
# df.to_csv('purchases.csv')

# viewing data
# df = pd.read_csv('appliances_rating.csv') #, index_col=0)
# print(df.head()) # optional number
# print(df.tail())
# print(df.columns)
# rename columns
# df.rename(columns={
#         'no': 'unique_id'
#     }, inplace=True)
# print(df.columns)
# df.columns = [col.upper() for col in df]
# print(df.columns)

# info and shape of dataframe
# df = pd.read_csv('appliances_rating.csv')
# df.info()
# print(df.shape)

# remove duplicates
# df = df.append(df)
# print(df.shape)
# df.drop_duplicates(inplace=True, keep='first')  # first, last, False
# print(df.shape)


# missing with values
# df = pd.read_csv('appliances_rating.csv')
# print(df.isnull())
# print(df.isnull().sum())
# df.dropna()  # NaN
# df.dropna(axis=1)
# rating = df['rating']
# rm = rating.mean()
# rating.fillna(rm, inplace=True)  # imputation
# print(type(rating))
# print(type(df[['no', 'rating']]))

# index slicing filter
# df = pd.read_csv('appliances_rating.csv')
# print(df.loc[0])
# print(df.iloc[1:7])
# df_new = df[(df.rating == 4) & (df.appliance_type == 'home')]
# print(df_new.count())


# def rating_function(x):
#     if x > 3:
#         return "good"
#     else:
#         return "bad"
#
# df["rating_category"] = df["rating"].apply(rating_function)
# print(df.head(2))

