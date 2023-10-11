from libraries import *
from constants import *

df = pd.read_csv("Results/tau_results_bootstrap_1000.csv", index_col=False).iloc[:,1:]
# for i in df.columns:
#     plt.hist(df[i])
#     plt.show()
bounds = np.percentile(df.values, [2.5, 97.5], axis=0)
pd.DataFrame(data=bounds, columns=lineage[1:], index=["Lower Bound", "Upper Bound"]).to_csv("Results/taus_95_confidence.csv")