#scikit-learn 機器學習常用的package, 以下是運用是大致上的架構
from sklearn.module import Model
model = Model() #build a model
model.fit(X, y) #x = independent variable(feature), dependent variable(target), xy = labeled data，讓他學習xy的範例
predictions = model.predict(X_new) #學習完，就給新的資料，讓他按照之前的做法執行，這邊舉例我們給了6則EMAIL的資料 = X_new，來預測是否有垃圾信件，x_new = unlabeled data
print(predictions) #結果是 array([0,0,0,0,1,0]) 說明有一封信是垃圾信件

#label data = training data

# k-Nearest Neighbors 常用於categories type target variable and classification problem
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
X = churn_df[['total_day_charge', 'total_eve_charge']].values
y = churn_df['churn'].values #churn是流失的意思(會員流失)，內容只有是或否
print(X.shape, y.shape) # (3333, 2), (3333,)

knn = KNeighborsClassifier(n_neighbors=15) #設定k=15
knn.fit(X, y)

#以上都是numpy array
X_new = np.array([[56.8, 17.5],[24.4, 24.1], [50.1, 10.9]]) #shape與 X 的column數是一樣的；以第一筆數值來做例子，56.8, 17.5，最接近這個點的15筆資料作鄰居，15筆裡有較多數是流失的樣本，所以被歸類為流失
predictions = knn.predict(X_new) 
print('Predictions: {}'.format(predictions)) #format中的東西會出現在{}中，這邊出來是[1,0,0]，代表流失、不流失、不流失

#檢驗預測是否正確，我們會把資料分成測試用，以及訓練用
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 21, stratify = y)
#一般test用的資料會佔0.2-0.3 = 20-30%, random_state = 設定種子，我們希望看到結果有多少流失，訓練跟測試也會有相近的流失值，所以以y作為分層
#train_test_split會return X_train, X_test, y_train, y_test 四個值
knn = KNeighborsClassifier(n_neighbors = 6)
knn.fit(X_train, y_train)
print(knn.score(X_test, y_test)) #.score是一種跟R^2差不多的東西

#要解釋k，可以了解模型複雜曲線
train_accuracies = {}
test_accuracies = {}
neighbors = np.arange(1, 26)
for neighbor in neighbors:
    knn = KNeighborsClassifier(n_neighbors=neighbor)
    knn.fit(X_train, y_train)
    train_accuracies[neighbor] = knn.score(X_train, y_train)
    test_accuracies[neighbor] = knn.score(X_test, y_test)

# Add a title
plt.title("KNN: Varying Number of Neighbors")
# Plot training accuracies
plt.plot(neighbors, train_accuracies.values(), label="Training Accuracy")
# Plot test accuracies
plt.plot(neighbors, test_accuracies.values(), label="Test Accuracy")
plt.legend()
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")

# Display the plot
plt.show()


#Regreeion learning
X = diabetes_df.drop('glucose', axis = 1) #feature
y = diabetes_df['glucose'] #target
X_bmi = X[:, 3]
print(y.shape, X_bmi.shape) #(752, ) (752, ) 兩個都是1D array，要2D先得
X_bmi = X_bmi.reshape(-1, 1)
print(X_bmi.shape) #(752, 1)

plt.scatter(X_bmi, y)
plt.ylabel("Blood Glucose (mg/dl)")
plt.xlabel('Body Mass Index')
plt.show()

from sklearn.linear_model import LinearRegression
reg = LinearRegression() #導入Model
reg.fit(X_bmi, y)
predictions = reg.predict(X_bmi) #會跑出預測的y值

plt.scatter(X_bmi, y)
plt.plot(X_bmi, predictions)
plt.ylabel("Blood Glucose (mg/dl)")
plt.xlabel('Body Mass Index')
plt.show()

#檢驗regression是否有效，第一種方法是用RSE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)
reg_all = LinearRegression()
reg_all.fit(X_train, y_train)
y_pred = reg_all.predict(X_test)
reg_all.score(X_test, y_test)

#第二種方法是MSE
from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_pred, squared = False)

#R^2可能會受到分拆資料的方式所影響，我們要用cross vaildation
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score, KFold
kf = KFold(n_splits = 6, shuffle = True, random_state = 42) #shuffle 會使在分拆前洗亂資料
reg = LinearRegression()
cv_results = cross_val_score(reg, X, y, cv = kf) #cv = 要折幾次
print(cv_results) #回傳的值是R^2
print(np.mean(cv_results), np.std(cv_results))
print(np.quantile(cv_results, 0.025))
print(np.quantile(cv_results, 0.975))
print(np.quantile(cv_results, [0.025, 0.975]))
print(pd.Series(cv_results).quantile([0.025, 0.975]))

#當regression a或b的係數太大，我們可以使用一些方法來regular 係數以避免過度fitting的問題
#Regularization 正則化: 1. Ridge regression 嶺回歸
from sklearn.linear_model import Ridge
scores = []
for alpha in [ 0.1, 1, 10, 100, 1000]: #試驗哪種alpha值最為合適
    ridge = Ridge(alpha = alpha)
    y_pred = ridge.predict(X_test)
    scores.append(ridge.score(X_test, y_test))
print(scores)

#Regularization 正則化: 2. Lasso regression 回歸
from sklearn.linear_model import Lasso
scores = []
for alpha in [ 0.1, 1, 10, 100, 1000]: #試驗哪種alpha值最為合適
    lasso = Lasso(alpha = alpha)
    lasso.fit(X_train, y_train)
    lasso_pred = lasso.predict(X_test)
    scores.append(lasso.score(X_test, y_test))
print(scores)

X = diabetes_df.drop('glucose', axis = 1).values #values可以直接只提取值
y = diabetes_df['glucose'].values
names = diabetes_df.drop('glucose', axis = 1).columns
lasso = Lasso(alpha = 0.1)
lasso_coef = lasso.fit(X, y).coef_ #coef可以直接提取係數
plt.bar(names, lasso_coef)
plt.xticks(rotation = 45)
plt.show() #結果顯示最能影響血糖的變項是糖尿病

##################檢驗模型的其他方法，除了準確度以外。也可以用Confusion matric中的 F1score 看看精確度與靈敏度
from sklearn.metrics import classification_report, confusion_matrix
knn = KNeighborsClassifier(n_neighbors = 7)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state = 42)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

##################Logistic regression model
from sklearn.linear_model import LogisticRegression
logis = LogisticRegression()
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.3, random_state = 12) 
logis.fit(X_train, y_train)
logis_pred = logis.predict(X_test)
y_pred_prob = logis.predict_proba(X_test)[:, 1] #計算y的機率，分為churned:no and churned:yes (churned是y)。[:, 1]代表取所有row但只要第2列的資料= churned:yes 的資料，整個就是只要churned:yes的機率的意思
print(y_pred_prob[0]) #[0.08961376] 代表churned:yes的機率是8.961%

#################### ROC curve 有助於了解TP FP與threshold之間的關係
from sklearn.metrics import roc_curve
fpr, tpr, threshold = roc_curve(y_test, y_pred_prob)
plt.plot([0,1], [0,1], 'k--')
plt.plot(fpr,tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Logistic Regression ROC curve')
plt.show()

#我們要知道這個model是不是能完美算出TP，FP = 0，我們便要計算AUC: 表示ROC的 area
from sklearn.metrics import roc_auc_score
print(roc_auc_score(y_test, y_pred_prob)) # 0.67，比用猜的好34%

#Hyperparameter tuning. 1. Grid Search cross validation
from sklearn.model_selection import GridSearchCV
kf = KFold(n_splits = 5, shuffle = True, random_state = 42)
param_grid = {'alpha': np.arange(0.0001,1,10),
              'solver': ['sag', 'lsqr']}
ridge = Ridge()
ridge_cv = GridSearchCV(ridge, param_grid, cv = kf)
ridge_cv.fit(X_train, y_train)
print(ridge_cv.best_params_, ridge_cv.best_score_) #生出最合適的alpha值

#hyperpararmeter tuning 2. Randomized Search CV
from sklearn.model_selection import RandomizedSearchCV
kf = KFold(n_splits = 5, shuffle = True, random_state = 42)
param_grid = {'alpha': np.arange(0.0001,1,10), #第三個數值是0.0001-1產生數字的數量，也可以用np.linspace(0.0001,1,10)
              'solver': ['sag', 'lsqr']}
ridge = Ridge()
ridge_cv = RandomizedSearchCV(ridge, param_grid, cv = kf, n_iter = 2) #用的模型, parameter, n_iter是可有可無的，用來指定有幾個parameter要被測試
ridge_cv.fit(X_train, y_train)
print(ridge_cv.best_params_, ridge_cv.best_score_)

test_score = ridge_cv.score(X_test, y_test)
print(test_score)

#example
# Import GridSearchCV
from sklearn.model_selection import GridSearchCV
# Set up the parameter grid
param_grid = {"alpha": np.linspace(0.00001, 1, 20)}
print(param_grid)
# Instantiate lasso_cv
lasso_cv = GridSearchCV(lasso, param_grid, cv=kf)
# Fit to the training data
lasso_cv.fit(X_train, y_train)
print("Tuned lasso paramaters: {}".format(lasso_cv.best_params_))
print("Tuned lasso score: {}".format(lasso_cv.best_score_))

# Create the parameter space
params = {"penalty": ["l1", "l2"],
         "tol": np.linspace(0.0001, 1.0, 50),
         "C": np.linspace(0.1, 1.0, 50),
         "class_weight": ["balanced", {0:0.8, 1:0.2}]} #會選出所有param裡數值最好的

# Instantiate the RandomizedSearchCV object
logreg_cv = RandomizedSearchCV(logreg, params, cv=kf)
# Fit the data to the model
logreg_cv.fit(X_train, y_train)
# Print the tuned parameters and score
print("Tuned Logistic Regression Parameters: {}".format(logreg_cv.best_params_))
print("Tuned Logistic Regression Best Accuracy Score: {}".format(logreg_cv.best_score_))


##### Dummy variable ######
#創建dummy variable 可以用sklearn OneHotEncoder() / pandas 的 get_dummies()
#用genre (categorical feature) 預測popularity (target variable)
#每一種genre會有其他變項的值，比如popularity、

from asyncio import as_completed
import pandas as pd
import numpy as np
from sklearn import pipeline
from sklearn.neighbors import KNeighborsClassifier
music_df = pd.read_csv('music.csv')
music_dummies = pd.get_dummies(music_df['genre'], drop_first = True) #drop_first可以說是自由度的概念，這邊是可以減1
print(music_dummies.head())
music_dummies = pd.concat([music_df, music_dummies], axis = 1) #把music_dummies併合到music_df裡
print(music_dummies)
music_dummies = music_dummies.drop('genre', axis = 1) #把原本的genre column del左
print(music_dummies)
music_dummies = pd.get_dummies(music_df, drop_first = True) #如果資料只有一個類別變項，就可以不指定column
print(music_dummies)


#我們也可以用sklearn來試試
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
X = music_dummies.drop('popularity', axis = 1).values
y = music_dummies['popularity'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
kf = KFold(n_splits = 4, shuffle = True, random_state = 42)
linreg = LinearRegression()
linreg_cv = cross_val_score(linreg, X_train, y_train, cv = kf, scoring = 'neg_mean_squared_error') #這樣會回應MSE回來，而因為cross_val數值R^2本身是正值且越高越好，MSE卻是越低越好，所以print出來會一個負值在前面
print(linreg_cv)
print(np.sqrt(-linreg_cv)) #RSS，加一個負號變回正值


#處理missing data
print(music_df.isna().sum().sort_values())

#我們可以選擇刪除佔數據不足5%的缺失觀察值
music_df = music_df.dropna(subset=['genre', 'popularity', 'loudness', 'liveness', 'tempo'])
#上述這些都是缺失值不足整體5%的
print(music_df.isna().sum().sort_values())

#data leakage = 心臟病預測心臟手術，有高相關，但我們用心臟手術預測心臟病雖然也會有高度關係，但一點意義都沒有，稱為data leakage

#另一種方法是用mean、median來取代缺失值，category則是用mode來取代
from sklearn.impute import SimpleImputer #impute 就是取代
X_cat = music_df['genre'].values.reshape(-1, 1) #執行缺失值的處理時，應要把不同種類的資料分開來
X_num = music_df.drop(['genre', 'popularity'], axis = 1).values
y = music_df['popularity'].values
X_train_cat, X_test_cat, y_train_cat, y_test_cat = train_test_split(X_cat, y, test_size = 0.2, random_state = 12)
X_train_num, X_test_num, y_train_num, y_test_num = train_test_split(X_num, y, test_size = 0.2, random_state = 12)
imp_cat = SimpleImputer(strategy='most_frequent') #默認是NA
X_train_cat = imp_cat.fit_transform(X_train_cat)
X_test_cat = imp_cat.transform(X_test_cat)
imp_num = SimpleImputer() #默認用平均數填滿na值
X_train_num = imp_num.fit_transform(X_train_num)
X_test_num = imp_num.transform(X_test_num)
X_train = np.append(X_train_num, X_train_cat, axis = 1)
X_test = np.append(X_test_num, X_test_cat, axis = 1)

from sklearn.pipeline import Pipeline #可以把處理資料的節點結合起來，史資料自動按照步驟去進行
music_df = music_df.dropna(subset=['genre', 'popularity', 'loudness', 'liveness', 'tempo'])
music_df['genre'] = np.where(music_df['genre'] = 'Rock', 1 , 0) #找找music_df['genre']裡的東西是不是Rock，是則1，不是則0
X = music_df.drop('genre', axis = 1).values
y = music_df['genre'].values

steps = [('imputation', SimpleImputer()),
         ('Logistic_Regression', LogisticRegression())]

pipeline = Pipeline(steps)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state = 12)
pipeline.fit(X_train, y_train)
pipeline.score(X_test, y_test)

######## 使資料能比較 ########
#1.標準化 2. 歸一化 3. 常態化
#標準化是指Z-SCORE這種標準化系數
#歸一化是每個數減去資料的最小值除以最大值減去最小值
#常態化

from sklearn.preprocessing import StandardScaler
X = music_df.drop('genre', axis =1)
y = music_df['genre'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 12)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print(np.mean(X), np.std(X))
print(np.mean(X_train_scaled), np.std(X_train_scaled))

step = [('scaler', StandardScaler()), ('knn', KNeighborsClassifier(n_neighbors= 6))]
pipeline = Pipeline(step)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 12)
knn_scaled = pipeline.fit(X_train, y_train)
y_pred = knn_scaled.predict(X_test)
print(knn_scaled.score(X_test, y_test))
knn_unscaled = KNeighborsClassifier(n_neigbhors = 6).fit(X_train, y_train)
print(knn_unscaled.score(X_test, y_test))

from sklearn.model_selection import GridSearchCV
steps = [('scaler', StandardScaler()),
         ('knn', KNeighborsClassifier())]
pipeline = Pipeline(steps)
parameters = {'knn__n_neighbors': np.arage(1, 50)} #__是指knn裡的東西，這邊是n_neighbors
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)
cv = GridSearchCV(pipeline, param_grid=parameters)
cv.fit(X_train, y_train)
y_pred = cv.predict(X_test)
print(cv.best_score_)
print(cv.best_params_)

#Classification
#畫圖
import matplotlib.pyplot as plt
#處理數據: 標準化、驗證模型
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, KFold, train_test_split
#預測模型
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

X = music.drop('genre', axis = 1).values
y = music['genre'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
models = {'Logistic Regression': LogisticRegression(), 'KNN': KNeighborsClassifier(), 'Decision Tree': DecisionTreeClassifier()}
results = []
for model in models.values(): #要 run function就要用values() function
    kf = KFold(n_splits = 6, random_state = 42, shuffle = True)
    cv_results = cross_val_score(model, X_train_scaled, y_train, cv = kf)
    results.append(cv_results)
plt.boxplot(results, labels = models.keys())
plt.show()

for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    test_score = model.score(X_test_scaled, y_test)
    print('{} Test Set Accuracy: {}'.format(name, test_score))

#Continuous
models = {"Linear Regression": LinearRegression(), "Ridge": Ridge(alpha=0.1), "Lasso": Lasso(alpha=0.1)}
results = []
# Loop through the models' values
for model in models.values():
  kf = KFold(n_splits=6, random_state=42, shuffle=True)
  # Perform cross-validation
  cv_scores = cross_val_score(model, X_train, y_train, cv=kf)
  # Append the results
  results.append(cv_scores)
# Create a box plot of the results
plt.boxplot(results, labels=models.keys())
plt.show()

# Import mean_squared_error
from sklearn.metrics import mean_squared_error
for name, model in models.items():
  # Fit the model to the training data
  model.fit(X_train_scaled, y_train)
  # Make predictions on the test set
  y_pred = model.predict(X_test_scaled)
  # Calculate the test_rmse
  test_rmse = mean_squared_error(y_test, y_pred, squared= False)
  print("{} Test Set RMSE: {}".format(name, test_rmse))