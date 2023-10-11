from libraries import *
from constants import *

df = pd.read_csv("Results/tau_results_bootstrap_1000.csv", index_col=False).iloc[:,1:]

coords = [(i,j) for i in range(4) for j in range(3)]
fig, ax = plt.subplots(4, 3, figsize=(8, 8))
for i in range(len(df.columns)):
    ax[coords[i]].hist(df[df.columns[i]], bins=100)
    ax[coords[i]].set_title(df.columns[i])
plt.subplots_adjust(hspace=0.5)
plt.show()

bounds = np.percentile(df.values, [2.5, 97.5], axis=0)
pd.DataFrame(data=bounds, columns=lineage[1:], index=["Lower Bound", "Upper Bound"]).to_csv("Results/taus_95_confidence.csv")
