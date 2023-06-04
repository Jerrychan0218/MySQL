#首先，導入檔案
import pandas as pd
cc_apps = pd.read_csv('crx.data', header = None)
print(cc_apps.head(5))
#先看看資料的基本資料
cc_apps_d = cc_apps.describe()
print(cc_apps_d)
cc_apps_in = cc_apps.info()
print(cc_apps_in)
#看看有沒有遺漏值
print(cc_apps.isna().sum()) #顯示15行都沒有NA值

#把資料分成train, test兩分
from sklearn.model_selection import train_test_split
cc_apps = cc_apps.drop([11, 13], axis = 1) #刪掉11及13 column，這邊因為沒有取名，所以沒有''
cc_apps_train, cc_apps_test = train_test_split(cc_apps, test_size = 0.33, random_state = 42)

#分完之後，我們看見有些缺失值原來是用 ? 來代替，所以要取代一下
import numpy as np
cc_apps_train = cc_apps_train.replace('?', np.NaN)
cc_apps_test = cc_apps_test.replace('?', np.NaN)

#Continuous variance 用 meean 來 fillna
cc_apps_train.fillna(cc_apps_train.mean(), inplace=True) #inplace是直接取代
cc_apps_test.fillna(cc_apps_train.mean(), inplace=True)
print(cc_apps_train.isnull().sum())
print(cc_apps_test.isnull().sum())

print(cc_apps_train[1].value_counts()) #出現最多的是23.58，共 6 次

#全部category variance 用mode 來 fillna 
for col in cc_apps_train:
    if cc_apps_train[col].dtypes == 'object':
        cc_apps_train = cc_apps_train.fillna(cc_apps_train[col].value_counts().index[0]) #index 是23.58, values是6，表示23.58有6次
        cc_apps_test = cc_apps_test.fillna(cc_apps_test[col].value_counts().index[0]) 

print(cc_apps_train.isnull().sum())
print(cc_apps_test.isnull().sum())

cc_apps_train = pd.get_dummies(cc_apps_train) #讀取dummies variable
cc_apps_test = pd.get_dummies(cc_apps_test)

cc_apps_test = cc_apps_test.reindex(columns=cc_apps_train.columns, fill_value=0)

print(cc_apps_test.head(5))

#MinMaxScaler 是一種scaling
from sklearn.preprocessing import MinMaxScaler
print(cc_apps_train.iloc[:, :12])
X_train, y_train = cc_apps_train.iloc[:, :-1].values, cc_apps_train.iloc[:,[-1]].values #cc_apps_train.iloc[:, :-1].values, 
X_test, y_test = cc_apps_test.iloc[:, :-1].values, cc_apps_test.iloc[:,[-1]].values

scaler = MinMaxScaler()
rescaledX_train = scaler.fit_transform(X_train) #scaling X_train
rescaledX_test = scaler.transform(X_test)

#回歸分析
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression() #讀取model
logreg.fit(rescaledX_train, y_train)


#透過confusion matrix了解模型準確度
from sklearn.metrics import confusion_matrix
y_pred = logreg.predict(rescaledX_test)
print("Accuracy of logistic regression classifier: ", logreg.score(rescaledX_test, y_test)) #跑出R^2
print(confusion_matrix(y_test, y_pred))

#利用GridSearchCV 嘗試找出最為合適的模型參數
from sklearn.model_selection import GridSearchCV
tol = [0.01, 0.001, 0.0001]
max_iter = [100, 150, 200]
param_grid = dict(tol = tol, max_iter = max_iter)

#GridSearchCV需要輸入
grid_model = GridSearchCV(estimator= logreg, param_grid=param_grid, cv = 5) #cv是要折幾次，一般會在之前就用KFold來設定好
grid_model_result = grid_model.fit(rescaledX_train, y_train)

best_score, best_params = grid_model_result.best_score_, grid_model_result.best_params_
print("Best: %f using %s" % (best_score, best_params))

best_model = grid_model_result.best_estimator_
print(best_model)
print("Accuracy of logistic regression classifier: ", best_model.score(rescaledX_test, y_test))
