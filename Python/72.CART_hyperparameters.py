#hyperparameters max_depth, min_samples_leaf, spliting criterion
#accuracy for classification，R^2 for regression

#cross_val_score 用來評估模型generation 的能力

#Grid search 找出最合適的參數

from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

SEED = 1

dt = DecisionTreeClassifier(random_state = SEED)

print(dt.get_params())#看看dt可以填哪些參數

params_dt = {
    'max_depth': [3,4,5,6],
    'min_samples_leaf': [0.04, 0.06, 0.08],
    'max_features': [0.2, 0.4, 0.6, 0.8]
}

grid_dt = GridSearchCV(estimator = dt, param_grid = params_dt, scoring = 'accuracy', cv = 10, n_jobs = -1)

grid_dt.fit(X_train, y_train)

best_hyperparams = grid_dt.best_params_
best_CV_Score = grid_dt.best_score_
best_model = grid_dt.best_estimator_
test_acc = best_model.score(X_test, y_test)
print(best_hyperparams)
print(best_CV_Score)
