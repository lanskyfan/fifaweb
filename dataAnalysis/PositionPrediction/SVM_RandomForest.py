import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
# from sklearn.metrics import plot_confusion_matrix

data = pd.read_csv(r"data.csv")



def pos(s):
    if re.findall("F$", s) or re.findall("T$", s) or re.findall("S$", s) or re.findall("W$", s):
        return 1  # Forward Player
    elif re.findall("M$", s):
        return 2  # Midfielder
    elif re.findall("B$", s):
        return 3  # Defense Player
    elif s == "GK":
        return 4  # GoalKeeper
    return 0  # In case, no value is present in data for prediction



# Correlation Map
data['General Position'] = pd.Series(list(map(pos,
                                              data['Position'].astype(str).tolist())))
data['General Position'].head(10)
fig = plt.figure()
fig.suptitle('Corelation Heatmap for player statistics FIFA 19', fontsize=20)
ax = sns.heatmap(data[['Overall', 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
                       'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
                       'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower',
                       'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
                       'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
                       'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
                       'GKKicking', 'GKPositioning', 'GKReflexes', 'Release Clause']].corr(), cmap=sns.diverging_palette(240, 10))





from sklearn.model_selection import train_test_split
from matplotlib import cm
from sklearn.neighbors import KNeighborsClassifier as knn_c
l = ['Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
     'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
     'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower',
     'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
     'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
     'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
     'GKKicking', 'GKPositioning', 'GKReflexes']
X = data[l].fillna(0.0)
y = data['General Position']
X.head(15)



X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)





# # SVM
# from sklearn.svm import SVC
# import time
# st = time.time()
# svcc = SVC(kernel='linear')
# svcc.fit(X_train, y_train)
# print('SVC TEST SCORE')
# print(svcc.score(X_test, y_test))
# print('------------------')
# print('SVC TRAINING SCORE')
# print(svcc.score(X_train, y_train))
# print("--- %s seconds ---" % (time.time() - st))






# Random Forest
#model with 1000 decision trees
st = time.time()
rf = RandomForestClassifier(n_estimators=1000, random_state=42)
rf.fit(X_train, y_train)
print('Random Forest TEST SCORE')
print(rf.score(X_test, y_test))
print('------------------')
print('Random Forest TRAINING SCORE')
print(rf.score(X_train, y_train))
print("--- %s seconds ---" % (time.time() - st))



# # Test Score Comparison
# y_pred = rf.predict(X)
# print('RF ACCURACY -')
# print(accuracy_score(y, y_pred))
# print('In comparision SVC accuracy is ' +
#       str(accuracy_score(y, svcc.predict(X))))





# Confusion Matrix
cm = confusion_matrix(y, rf.predict(X))
cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
df_cm = pd.DataFrame(cm)
plt.suptitle('Normalized Confusion Matrix', fontsize=20)
sns.set(font_scale=1.4)  # for label size
sns.heatmap(df_cm, annot=True, annot_kws={"size": 16})  # font size

plt.show()
