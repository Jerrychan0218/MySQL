#Randomforest bootstrap 改超參數，可能只會有一點點的變化
from sklearn.ensemble import RandomForestRegressor

SEED = 1
rf = RandomForestRegressor(random_state = SEED)

rf.get_params()

#train_test_split

from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import GridSearchCV

params_rf = {'n_estimators':[300,400,500],
             'max_depth': [4, 6, 8],
             'min_samples_leaf': [0.1, 0.2],
             'max_features': ['log2', 'sqrt']
            }

grid_rf = GridSearchCV(estimator = rf, param_grid = params_rf, cv = 3, scoring='neg_mean_squared_error', verbose = 1, n_jobs = -1) #verbose 是步驟詳細描述的程度，越高越詳細

grid_rf.fit(X_train, y_train)

best_hyperparams = grid_rf.best_params_
print(best_hyperparams)

best_model = grid_rf.best_estimator_
y_pred = best_model.predict(X_test)

rmse_test = MSE(y_test, y_pred)** (1/2)
print(rmse_test)