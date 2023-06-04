#Load module
from pydoc import describe
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

#read csv
test_data = pd.read_csv('test.csv')
train_data = pd.read_csv('train.csv')
result = pd.read_csv('gender_submission.csv')

#data description
print(train_data.info())
print(train_data.describe())
print(train_data.head())

#Missing data
print(train_data.isna().sum())

#train missing
m_age_mean = train_data.groupby('Sex')['Age'].mean()['male']
f_age_mean = train_data.groupby('Sex')['Age'].mean()['female']

# for age
def fill_age(sex_age):
    sex = sex_age[0]
    age = sex_age[1]

    if pd.isnull(age):
        if 'male' in sex:
            return m_age_mean
        if 'female' in sex:
            return f_age_mean
    else:
        return age

train_data['Age'] = train_data[['Sex', 'Age']].apply(fill_age, axis = 1)

#for sex
sex={'male':0, 'female':1}
train_data = train_data.replace({'Sex':sex})

#for cabin
train_data.drop('Cabin', axis = 1, inplace = True)

#for Embarked
print(train_data['Embarked'].mode())
train_data['Embarked'].fillna('S', inplace = True)

#plot catagory variable and numeric
print(train_data.isna().sum())
print(train_data['Survived'].value_counts())
cate = ['Survived', 'Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked']
num = ['Age', 'Fare']

for i in cate:
    catplot = sns.countplot(train_data[i])
    plt.title(i)
    plt.show()

for a in num:
    numplot = sns.histplot(train_data[a])
    plt.title(a)
    plt.show()

# plt.figure(figsize=(10,8))
# sns.scatterplot(data = train_data, x = 'Age', y = 'Fare', hue = 'Survived')
# plt.show()

# train_data['Name_cat'] = train_data.Name.apply(lambda x: x.split(',')[1].split('.')[0].strip())
# print(train_data['Name_cat'].value_counts())

train_data.drop(['Name', 'Ticket','Embarked'], axis = 1, inplace = True)
print(train_data.head())

#Test data
print(test_data.info())
print(test_data.describe())
print(test_data.head())

#Missing data
print(test_data.isna().sum())

#Fill age
f_age_test = test_data.groupby('Sex')['Age'].mean()[0]
m_age_test = test_data.groupby('Sex')['Age'].mean()[1]

test_data['Age'] = test_data[['Sex', 'Age']].apply(fill_age, axis = 1)

#for sex
sex={'male':0, 'female':1}
test_data = test_data.replace({'Sex':sex})

#fill fare
test_data['Fare'].fillna(test_data['Fare'].mean(), inplace = True)

#drop cabin
test_data.drop(['Cabin', 'Name', 'Ticket', 'Embarked'], axis = 1, inplace = True)
feature = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
print(test_data.isna().sum())

#train & test
cate_train = ['Survived', 'Pclass', 'Sex', 'SibSp', 'Parch']
train_data[cate_train] = train_data[cate_train].astype('category')
pd.get_dummies(train_data, drop_first = True)



# cate_test = ['Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked']
# test_data[cate_test] = test_data[cate_test].astype('category')
# X_test = pd.get_dummies(test_data, drop_first = True)
# print(X_test.head())

#Standardize
stand = StandardScaler()
train_data[['Age', 'Fare']] = stand.fit_transform(train_data[['Age', 'Fare']])
# X_test[['Age', 'Fare']] = stand.transform(X_test[['Age', 'Fare']])
X = train_data.drop('Survived', axis = 1)
y = train_data['Survived']

X_train, X_ex, y_train, y_ex = train_test_split(X[feature], y, test_size=0.2, random_state=10,stratify = y)

logit = LogisticRegression(random_state=10)
logit.fit(X_train, y_train)
y_pred = logit.predict(X_ex)
acc = accuracy_score(y_ex, y_pred)
print(acc)

dt = DecisionTreeClassifier(max_depth=6, random_state=10)
dt.fit(X_train, y_train)
y_pred1 = dt.predict(X_ex)
acc1 = accuracy_score(y_ex, y_pred1)
print(acc1)

ada = AdaBoostClassifier(base_estimator = dt, n_estimators= 1000, random_state = 10)
ada.fit(X_train, y_train)
y_pred2 = ada.predict(X_ex)
acc2 = accuracy_score(y_ex, y_pred2)
print(acc2)

#Prediction
pred_f = dt.predict(test_data[feature])
output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived':pred_f})
output.to_csv('dt.csv', index = False)




