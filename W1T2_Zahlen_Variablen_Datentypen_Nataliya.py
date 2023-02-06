import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme('notebook', style='dark') #darkgrid, whitegrid, dark, white, ticks
plt.style.use("dark_background")

# # Load the example planets dataset
# from sklearn import datasets
# from sklearn.decomposition import PCA
#
# # import some data to play with
# iris = datasets.load_iris()
# df = pd.DataFrame(data=iris.data,
#                   columns=iris.feature_names)
# print(df.head())
# X = iris.data[:, :2]  # we only take the first two features.
# cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
# # y = iris.target
# g = sns.relplot(
#     data=df,
#     x="sepal length (cm)", y="sepal width (cm)",
#     hue="petal length (cm)", size="petal width (cm)",
#     palette="vlag", sizes=(10, 200), # or cmap w/o "" or cmap=plt.cm.Set1, edgecolor="k"
# )
# g.set(xscale="log", yscale="log")
# g.ax.xaxis.grid(True, "minor", linewidth=.25)
# g.ax.yaxis.grid(True, "minor", linewidth=.25)
# g.despine(left=True, bottom=True)
# plt.show()

data = {'x': [1,2,3,4,5], 'y': [2,4,6,8,10]}
df = pd.DataFrame(data)
sns.lineplot(x='x', y='y', data=df)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Seaborn Lineplot')
plt.show()