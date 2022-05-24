
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from iris.helpers import load_iris_dataset, split

def classify_score(n_neighbors_start, n_neighbors_stop):
    iris_data = load_iris_dataset()

    x_train, x_test, y_train, y_test = split(iris_data)

    train_scores = []
    test_scores = []
    for k in range(n_neighbors_start, n_neighbors_stop):
        knn = KNeighborsClassifier(n_neighbors=k)

        knn.fit(x_train, y_train)

        y_pred_train = knn.predict(x_train)
        train_scores.append(accuracy_score(y_train, y_pred_train))

        y_pred_test = knn.predict(x_test)
        test_scores.append(accuracy_score(y_test, y_pred_test))

    return train_scores, test_scores
