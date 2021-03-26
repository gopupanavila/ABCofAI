import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score


# 3. Load red wine data.
dataset_url = 'winequality-red.csv'
data = pd.read_csv(dataset_url, sep=';')
print('Loaded red wine data')

# 4. Split data into training and test sets
# it's good practice to stratify your sample by the target variable
# test size here is 20%
y = data.quality
X = data.drop('quality', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state=123,
                                                    stratify=y)
print('Split the data into train and test set')

# 5. Declare data preprocessing steps
# standardize our features
# Standardization is the process of subtracting the means from each feature
# and then dividing by the feature standard deviations
# Many algorithms assume that all features are centered around zero
# and have approximately the same variance.
# A modeling pipeline that first transforms the data using StandardScaler() and
# then fits a model using a random forest regressor
pipeline = make_pipeline(preprocessing.StandardScaler(),
                         RandomForestRegressor(n_estimators=100))
print('Pipeline got created')

# 6. Declare hyperparameters to tune
# Within each decision tree, the computer can empirically
# decide where to create branches based on either mean-squared-error (MSE)
# or mean-absolute-error (MAE)
# pipeline.get_params()
hyperparameters = {'randomforestregressor__max_features': ['auto', 'sqrt', 'log2'],
                   'randomforestregressor__max_depth': [None, 5, 3, 1]}

# 7. Tune model using cross-validation pipeline
# Cross-validation is a process for reliably estimating the performance of a method for
# building a model by training and evaluating your model multiple times using the same method
# clf.best_params_
clf = GridSearchCV(pipeline, hyperparameters, cv=10)
clf.fit(X_train, y_train)
print('Tuned the model')

# 8. Refit on the entire training set
# No additional code needed if clf.refit == True (default is True)

# 9. Evaluate model pipeline on test data
pred = clf.predict(X_test)
print(pred)
print(r2_score(y_test, pred))
print(mean_squared_error(y_test, pred))

