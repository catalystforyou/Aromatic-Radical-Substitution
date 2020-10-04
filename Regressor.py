import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import svm, neighbors, tree
import numpy as np
import matplotlib.patches as mpatches
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, GridSearchCV
import time

df = pd.read_csv('merge_table.csv')
data = df.drop(['Atom', 'yield'], axis=1)
scaler = StandardScaler()
scaler.fit(data)
data = scaler.transform(data)
label = df['yield']
X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=0.3, random_state=np.random.randint(1,10000))
model = RandomForestRegressor(n_estimators=50)
# model = LinearRegression()
#model= tree.DecisionTreeRegressor()
model.fit(X_train, y_train)
vld = model.predict(X_train)
preds = model.predict(X_test)
#r_squared = r2_score(y_test, preds)
train_r2_score = model.score(X_train, y_train)
r2_score = model.score(X_test, y_test)
train_rmse = mean_squared_error(y_train, vld) ** 0.5
rmse = mean_squared_error(y_test, preds) ** 0.5
plt.figure(figsize=(5, 5))
#r2_patch = mpatches.Patch(label="R2={:04.2f}".format(r_squared))
train_rmse_patch = mpatches.Patch(label="TRAIN_RMSE={:04.2f}".format(train_rmse))
rmse_patch = mpatches.Patch(label="RMSE={:04.2f}".format(rmse))
train_r2_score = mpatches.Patch(label="TRAIN_r2={:04.2f}".format(train_r2_score))
r2_score = mpatches.Patch(label="r2={:04.2f}".format(r2_score))
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.scatter(vld, y_train, alpha=0.1)
stdline=np.arange(0,100,0.01)
plt.plot(stdline,stdline)
plt.scatter(preds, y_test, c='r', alpha=0.5)
plt.legend(handles=[rmse_patch, train_rmse_patch, r2_score, train_r2_score])
plt.show()
