#就是完全利用bootstraps 產生樣本，並按照training set的樣本再複製然後train model, 然後用來預測，而每個複製的樣本都會有d個  feature不會重複抽樣，好處是一般會比tree的variance要低

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE
import pandas as pd

SEED = 1

X_train. X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = SEED)
rf = RandomForestRegressor(n_estimators = 400, min_samples_leaf = 0.12, random_state = SEED) #min_samples_leaf = 0.12, 至少12%的sample用於training

importances_rf = pd.Series(rf.feature_importances_, index = X.columns)

sorted_importances_rf = importance_rf.sort_values()

sorted_importances_rf.plot(kind = 'barh', color = 'lightgreen') #barh是水平版的bar plot #用rf model來預測時，HR會是最為重要的feature

plt.show()

