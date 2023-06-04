#adaboost = adaptive boosting 與gradient boosting都是讓機器持續學習的function
#Adaboost關注在錯誤預測上，透過不斷改變前置作業來改善訓練，每一次的預測都會產生 alpha值，代表該次預測中的誤差，用來決定下一次訓練的權重
#而在adaboost裡有一個參數 eta 來調整 alpha值，如果eta太小，應該要用更多次的預測來彌補
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

SEED = 1

X_train, y_train, X_test, y_test = train_test_split(X, y, test_size = 0.3, stratify= y, random_state = SEED)

dt = DecisionTreeClassifier(max_depth=1, random_state=SEED)

adb_clf = AdaBoostClassifier(base_estimator=dt, n_estimators=100)

adb_clf.fit(X_train, y_train)

y_pred_proba = adb_clf.predict_proba(X_test)[:, 1] #要計算roc_auc_score就需要有postive的資料分布

adb_clf_roc_auc_score = roc_auc_score(y_test, y_pred_proba)

print(adb_clf_roc_auc_score)