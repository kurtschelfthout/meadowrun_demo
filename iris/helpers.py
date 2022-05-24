import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def load_iris_dataset():
    iris = load_iris()
    iris_data = pd.DataFrame(iris.data, columns=iris.feature_names)
    iris_data['target'] = iris.target
    return iris_data

def split(iris_data):
    x = iris_data.iloc[:,2:-1].values
    y = iris_data.iloc[:,-1].values
    return train_test_split(x, y, test_size=.20, random_state=42)