from libraries import *
from constants import *
from prepare_data import *

# From Before ------------------
def compute_total_counts(compartment):
    means = [np.mean(raw_label_counts[i][compartment] / label_frequency[i][compartment]) for i in timesteps]
    return np.mean(means) * 100

def compute_total_counts_median(compartment):
    lst = []
    for i in timesteps:
        temp = (raw_label_counts[i][compartment] / label_frequency[i][compartment]).replace(np.inf, np.nan).dropna()
    for j in range(temp.shape[0]):
        lst.append(temp.iloc[j])
    # plt.hist(lst,bins=20)
    # plt.show()
    return np.median(lst) * 100
# ------------------------------

def compute_counts_ratio(reference, upstream, mode):
    df_label = get_data_df("label")
    df_raw = get_data_df("raw")
    ratios = []
    for i in timesteps:
        ratios.append(((df_raw[i][reference] / df_label[i][reference]) / (df_raw[i][upstream] / df_label[i][upstream])).tolist())
    ratios = np.array(sum(ratios, []))
    ratios = ratios[np.isfinite(ratios)]
    ratios = ratios[~np.isnan(ratios)]
    if mode == "mean":
        return np.mean(ratios)
    elif mode == "median":
        return np.median(ratios)
    return None