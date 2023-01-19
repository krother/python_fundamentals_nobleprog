"""
Predict Bike sharing demand in Washington, D.C.

usage

    python -m pip install scikit-learn
    
a Machine Learning Example

https://www.kaggle.com/c/bike-sharing-demand/data


- hourly rental data spanning two years
- the training set is comprised of the first 19 days of each month, while the test set is the 20th to the end of the month
- goal: predict the total **count** of bikes rented during each hour covered by the test set, using only information available prior to the rental period
"""

import pandas as pd
from sklearn.preprocessing import FunctionTransformer
from sklearn.linear_model import PoissonRegressor
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# read training data
train = pd.read_csv('train.csv', parse_dates=[0])
print(train.head())


# make separate columns of date elements
def create_date_features(df):
    x = df['datetime']
    return pd.DataFrame({
        'month': x.dt.month,
        'hour': x.dt.hour,
        'week': x.dt.isocalendar().week,
        'weekday': x.dt.weekday
    })


# define rules to transform columns
datetime_pipeline = make_pipeline(
    FunctionTransformer(create_date_features, validate=False),
    OneHotEncoder(handle_unknown='ignore')
)

transformer = make_column_transformer(
    (datetime_pipeline, ['datetime']),
    (StandardScaler(), ['temp', 'humidity', 'windspeed']),         
    (OneHotEncoder(handle_unknown='ignore'), ['season', 'weather']),
    ('passthrough', ['workingday', 'holiday'])
)


# define the machine learning model
model_pipeline = make_pipeline(
    transformer, 
    PoissonRegressor(max_iter=1000)
)


# select columns for model input + output
X_train = train.drop(['casual','registered', 'count'], axis=1)
y_train = train['count']


# train the model
model_pipeline.fit(X_train, y_train)

# calculate a R^2 score
training_score = round(model_pipeline.score(X_train, y_train), 3)
print(training_score)


# make some predictions for new data (inference)
test = pd.read_csv('test.csv', parse_dates=[0])
test['prediction'] = model_pipeline.predict(test)
print(test.head())
