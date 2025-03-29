"""
Student Performance Prediction – Data Mining Final Project  
Adapted by Marc Ball

Original group project for CSC 535 – Data Mining (May 2024)

Description:  
Applies Random Forest, Neural Network, and Decision Tree Regression models  
to predict student test scores based on economic and environmental factors.

This version was adapted for individual portfolio use. Original group authorship removed  
to preserve anonymity. Functionality, code structure, and results remain aligned with the original submission.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score, r2_score, mean_squared_error
import matplotlib.pyplot as plt


def encode_categorical(data):
    '''
    gender,parental level of education,lunch,test preparation course hold raw strings
    we encode each possible value to an integer and return the new dataset
    '''
    for column in ['gender', 'parental level of education', 'lunch', 'test preparation course']:
        # Category is a data type in pandas
        # cat.codes returns the possible values each encoded to a number like id
        data[column] = data[column].astype('category').cat.codes 
    return data

def add_features(data):
    '''
    adds new columns to the dataset,
    '''
    data['average score'] = data[['math score', 'reading score', 'writing score']].mean(axis=1)
    return data

def plot_results(y_test, y_pred, model_type, score_type):

    # Plotting actual vs predicted values
    plt.figure(figsize=(10, 5))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.xlabel('Actual Scores')
    plt.ylabel(f'Predicted Scores')
    plt.title(f'{model_type} Actual vs Predicted for {score_type}')
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r')
    plt.show()


def train_and_evaluate(x_train, y_train, x_test, y_test, model_type, score_type):
    '''
    trains and tests the model depending on the model_type and score_type params
    '''
    if model_type in ['random forest', 'neural network']:
        y_train = y_train[score_type].tolist()
        y_test = y_test[score_type].tolist()
    
    if model_type == 'random forest':
        model = RandomForestRegressor(n_estimators=200, max_depth=None, min_samples_leaf=4, random_state=23)

    elif model_type == 'neural network':
        model = MLPRegressor(hidden_layer_sizes=(100,), activation='relu', solver='adam', max_iter=2000, random_state=23)

    elif model_type =='decision tree regression':
        model = DecisionTreeRegressor(random_state=23)
    
    # Train the model
    trained_model = model.fit(x_train, y_train)
    
    # Predict the test set results
    y_pred = trained_model.predict(x_test)
    
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'{model_type.title()} mean squared error for {score_type.title()}: {mse}')
    # print(f'{model_type} R^2 for {score_type}: {r2}')

    # if model_type == 'random forest':
    #     feature_importances = pd.Series(model.feature_importances_, index=X_train.columns)
    #     print(f'Feature Importances for {score_type}:')
    #     print(feature_importances.sort_values(ascending=False))

    # plot_results(y_test, y_pred, model_type, score_type)



def main():
    data = pd.read_csv('StudentsPerformance.csv')
    data_encoded = encode_categorical(data)
    data_encoded = add_features(data_encoded)

    scores = ['math score', 'reading score', 'writing score', 'average score']
    economic_features = ['parental level of education', 'lunch', 'test preparation course']

    for model_type in ['random forest', 'neural network', 'decision tree regression']:
        for score_type in scores:
            feature_columns = [col for col in data_encoded.columns if col in economic_features]
            score_columns = [col for col in data_encoded.columns if col == score_type]
            
            x = data_encoded[feature_columns]
            y = data_encoded[score_columns]
            # print(x) 
            # print(y)

            # Splits the data into training and testing sets
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=23)

            train_and_evaluate(x_train, y_train, x_test, y_test, model_type, score_type)
        

if __name__ == '__main__':
    main() 