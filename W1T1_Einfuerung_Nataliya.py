print("Hallo Welt!")

# dies ist ein einzeiliger Kommentar

"""
 dies ist 
 laengerer Kommentar
"""
# import sys
# sys.set_int_max_str_digits(100000)
# print(2 ** 131313)

"""
Unterstriche dienen der besseren Lesbarkeit langer Zahlen.
Im Alltag verwenden wir Tausender-Trennpunkte, um Dreierblöcke von Zahlen voneinander optisch zu trennen.
1.234.567
Bei Zahlen werden dazu Unterstriche verwendet. Regeln:
1) zwischen je zwei Ziffern nur je EIN Unterstrich: 1_234. Verboten: 1__234
2) keine führenden oder abschließenden Unterstriche: verboten: _13 oder 13_
3) unsinnig, aber erlaubt: 1_2_34_5
"""

"""
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Matplotlib Example')
plt.show()
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme('notebook', style='dark') #darkgrid, whitegrid, dark, white, ticks
plt.style.use("dark_background")

# Load the example planets dataset
from sklearn import datasets
from sklearn.decomposition import PCA

# import some data to play with
iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data,
                  columns=iris.feature_names)
print(df.head())
# X = iris.data[:, :2]  # we only take the first two features.
# y = iris.target

cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df,
    x="sepal length (cm)", y="sepal width (cm)",
    hue="petal length (cm)", size="petal width (cm)",
    palette="vlag", sizes=(10, 200), # or cmap w/o "" or cmap=plt.cm.Set1, edgecolor="k"
)
g.set(xscale="log", yscale="log")
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)
plt.show()

