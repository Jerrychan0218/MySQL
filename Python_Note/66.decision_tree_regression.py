from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE

X_train, X_test, y_train, y_test = (X, y, test_size = 0.2, random_state = 3)

#min_samples_leaf = 0.1 是指每個葉子必須包含至少10%的訓練數據
dt = DecisionTreeRegressor(max_depth = 4, min_samples_leaf =0.1, random_state = 3)

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import cross_val_score

SEED = 123
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = SEED)
dt = DecisionTreeRegressor(max_depth = 4, min_samples_leaf = 0.14, random_state = SEED)
MSE_CV = - cross_val_score(dt, X_train, y_train, cv = 10, scoring = 'neg_mean_squared_error', n_job = -1) #cv = 10 = 折10次, 'neg_mean_squared_error' 計算負的MSE，因為CVScore function不能計算正值
#所以在開頭加了 - 來讓它變為正，n_jobs = -1 可以利用全部cpu來計算
dt.fit(X_train, y_train)
y_predict_train = dt.predict(X_train)
y_predict_test = dt.predict(X_test)
print('CV mse:{}',format(MSE_CV.mean())) # 20.51
print('Train MSE:{}'.format(MSE(y_train, y_predict_train))) #15.30 CVMSE > train MSE 所以可以推斷是overfiting，可以減少model複雜度或是增加 min_samples_leaf 來解決一下
print('Test MSE:'.format(MSE(y_test, y_predict_test))) #20.92

