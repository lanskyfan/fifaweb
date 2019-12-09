import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from tqdm import tqdm


data = pd.read_csv(r"code\fifa19data444.csv")
print(data.head())
print(data.describe())


data['Nationality'].value_counts()[:15].plot(kind='bar')
plt.show()



data['Difference'] = data['Potential']-data['Overall']

# def evolution(d):
#     if d == 0:
#         return 'Stable'
#     elif d > 1 and d <= 5:
#         return 'Small'
#     elif d > 6 and d <= 10:
#         return 'Medium'
#     elif d > 10:
#         return 'Large'

# data['Evolution'] = data['Difference'].apply(evolution)
# # MOST PROMISING YOUTH PLAYER WHO HAVE A VERY HIGH POTENTIAL:
# promising = data.loc[(data['Evolution'] == 'Large') & (data['Potential'] > 85)].sort_values(by='Potential', ascending=False)[:10]
# cols = ['Name', 'Club', 'Overall', 'Age', 'Potential', 'Value']
# print(promising[cols])


# # Plot
# sns.countplot(data['Preferred Foot'])
# plt.title('Player Preferred Foot')
# plt.show()

# plt.figure(figsize=(15, 10))
# sns.countplot(data['Position'])
# plt.title('Number of Players per Position')
# plt.show()







from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
# from sklearn.decomposition import PCA


data = pd.read_csv(r'code\fifa19data444.csv')
# print(data.columns)
# attributes = data.iloc[:, 54:83]

attributes = data.iloc[:, 19:48]
attributes['Skill Moves'] = data['Skill Moves']
# workrate = data['Work Rate'].str.get_dummies(sep='/ ')
# attributes = pd.concat([attributes, workrate], axis=1)
df = attributes.copy()
# attributes = attributes.dropna()
df['Name'] = data['Name']
df['ID'] = data['ID']
df = df.dropna()
print(attributes.columns, '\n')
print(attributes.head())
# print(df.head())

scaled = StandardScaler()
X = scaled.fit_transform(attributes)
recommendations = NearestNeighbors(n_neighbors = 6, algorithm = 'ball_tree')
recommendations.fit(X)
player_index = recommendations.kneighbors(X)[1]


def get_index(x):
    return df[df['Name'] == x].index.tolist()[0]

def recommend_me(player):
    print("5 Players similar to {} are : ".format(player))
    index = get_index(player)
    # index = player
    for i in player_index[index][1:]:
        print(df.iloc[i]['Name'])


recommend_me('L. Messi')









recommend_list1 = []
recommend_list2 = []
recommend_list3 = []
recommend_list4 = []
recommend_list5 = []


def recommend(index):
    # print("5 Players similar to {} are : ".format(index))
    # print(player_index[index][1:])

    # for i in player_index[index][1:]:
    #     print(df.iloc[i]['ID'])

    i = player_index[index][1:][0]
    recommend_list1.append(df.iloc[i]['ID'])

    i = player_index[index][1:][1]
    recommend_list2.append(df.iloc[i]['ID'])

    i = player_index[index][1:][2]
    recommend_list3.append(df.iloc[i]['ID'])

    i = player_index[index][1:][3]
    recommend_list4.append(df.iloc[i]['ID'])

    i = player_index[index][1:][4]
    recommend_list5.append(df.iloc[i]['ID'])




# for i in tqdm(range(df.shape[0])):
#     recommend(i)


# recommend_data = pd.DataFrame({
#     'ID': df['ID'],
#     'Similar Player 1 ID': recommend_list1,
#     'Similar Player 2 ID': recommend_list2,
#     'Similar Player 3 ID': recommend_list3,
#     'Similar Player 4 ID': recommend_list4,
#     'Similar Player 5 ID': recommend_list5,
# })
# recommend_data.to_csv('Recommend Player Data.csv', index=False)


# print(recommend_list1)
# print(recommend_list2)
# print(recommend_list3)
# print(recommend_list4)
# print(recommend_list5)

def results_to_csv(list1, list2, list3, list4, list5, list6):
    # y_test = y_test.astype(int)
    df = pd.DataFrame({'Category': y_test,
                       })
    df.index += 1  # Ensures that the index starts at 1.
    df.to_csv('submission.csv', index_label='Id')
