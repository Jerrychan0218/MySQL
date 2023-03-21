#是一個現在很流行的boosting
#沒有權重調整，用前次預測的殘差來預測下次，前次預測的殘差，減掉這次預測的殘差
#也有eta做為調整殘差影響
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE

SEED = 1

X_train, y_train, X_test, y_test = train_test_split(X,y, test_size = 0.3, random_state = SEED)
gbt = GradientBoostingRegressor(n_estimators = 300, max_depth = 1, random_state = SEED)
#fit predict MSE RMSE


#Stochastic Gradient Boosting 隨機版，只有部分feature會被納入一次預測中
# Import GradientBoostingRegressor
from sklearn.ensemble import GradientBoostingRegressor
# Instantiate sgbr
sgbr = GradientBoostingRegressor(max_depth=4, 
            subsample=0.9,
            max_features=0.75,
            n_estimators=200,
            random_state=2)

# Fit sgbr to the training set
sgbr.fit(X_train, y_train)

# Predict test set labels
y_pred = sgbr.predict(X_test)

# Import mean_squared_error as MSE
from sklearn.metrics import mean_squared_error as MSE
# Compute test set MSE
mse_test = MSE(y_test, y_pred)
# Compute test set RMSE
rmse_test = mse_test ** (1/2)
# Print rmse_test
print('Test set RMSE of sgbr: {:.3f}'.format(rmse_test))