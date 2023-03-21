#Bagging就是運用bootstapping技術來整合預測，跟ensemble learning是同一種東西，可以用於classification and Regression上

from sklearn.ensemble import BaggingClassifier #for regression BaggingRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

SEED = 1

X_train,y_train,X_test,y_test = train_test_split(X, y, test_size = 0.3, stratify=y, random_state = SEED)

dt = DecisionTreeClassifier(min_samples_leaf=0.16, max_depth = 4, random_state = SEED)

bc = BaggingClassifier(base_estimator=dt, n_estimators= 300, oob_score = True, n_job = -1) #n_job =-1 所有CPU用於計算, oob_score可以驗證bc測量是否準確，而不用使用cross_val_

bc.fit(X_train, y_train)
y_pred = bc.predict(X_test)
accuracy_score(y_test, y_pred)
oob_acc = bc.oob_score_
#fit(train), predict, accuracy_score