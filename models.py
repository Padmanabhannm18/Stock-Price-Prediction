import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.linear_model import BayesianRidge
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

def train_and_evaluate_models(x_train, y_train, x_test, y_test):
    """Trains multiple regression models and evaluates their performance."""
    models = {
        "Decision Tree": {
            "model": DecisionTreeRegressor(),
            "params": {
                "max_depth": [None, 10, 20],
                "min_samples_split": [2, 5]
            }
        },
        "Random Forest": {
            "model": RandomForestRegressor(),
            "params": {
                "n_estimators": [50, 100],
                "max_depth": [None, 10],
                "min_samples_split": [2, 5]
            }
        },
        "K-Nearest Neighbors": {
            "model": KNeighborsRegressor(),
            "params": {
                "n_neighbors": [3, 5],
                "weights": ["uniform", "distance"]
            }
        },
        "Support Vector Machine": {
            "model": SVR(),
            "params": {
                "kernel": ["linear", "rbf"],
                "C": [1, 10],
                "gamma": [0.1, 1]
            }
        },
        "Bayesian Ridge": {
            "model": BayesianRidge(),
            "params": {}
        },
        "Gradient Boosting": {
            "model": GradientBoostingRegressor(),
            "params": {
                "n_estimators": [100, 200],
                "learning_rate": [0.1, 0.2],
                "max_depth": [3, 5]
            }
        }
    }

    best_model = None
    best_r2 = float('-inf')
    best_model_name = ""
    results = {}

    for name, model_info in models.items():
        grid = GridSearchCV(model_info["model"], model_info["params"], cv=3, scoring="r2")
        grid.fit(x_train, y_train)
        best_estimator = grid.best_estimator_
        y_pred = best_estimator.predict(x_test)
        r2 = r2_score(y_test, y_pred)
        results[name] = {
            "R2": r2,
            "Best Params": grid.best_params_,
            "Model": best_estimator
        }

        if r2 > best_r2:
            best_r2 = r2
            best_model = best_estimator
            best_model_name = name

    return best_model, best_model_name, best_r2, results
