#CART classification and regression tree 會有一些缺點：容易overfit、只能正交、對於train set的變化非常敏感，emsemble learning(集成學習)或許可以解決這方面問題
#ensemble learning用一個資料train很多不同模型，並用這些模型進行predict，然後整合模型的預測結果，結果更穩更不易出錯

#導入accuracy & split data
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

#導入用來預測的模型
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.ensemble import VotingClassifier

SEED = 1

X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=0.3, random_state = SEED)
lr = LogisticRegression(random_state = SEED)
knn = KNN()
dt = DecisionTreeClassifier(random_state = SEED)
classifiers = [('Logistic Regression', lr),('KNN', knn), ('Classification', dt)]

for i, f in classifiers:
    f.fit(X_train, y_train)
    y_pred = f.predict(X_test)
    print(accuracy_score(y_test, y_pred))

vc = VotingClassifier(estimators=classifiers)
vc.fit(X_train, y_train)
y_pred = vc.predict(X_test)
print(accuracy_score(y_test, y_pred))