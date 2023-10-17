from constants import *
from import_data import *

def preprocess_data(dataframe):
    # Removes incomplete record in last row of 9th month
    dataframe["9 months"] = dataframe["9 months"].iloc[:-1]
    # Removes incomplete records in last 3 rows of 12th month
    dataframe["12 months"] = dataframe["12 months"].iloc[:-3]
    return dataframe

def get_data_df(mode):
    df = get_data(mode)
    return preprocess_data(df)

def get_label_freq(bootstrap=False):
    df = get_data_df("label")

    x = []
    for i in range(len(timesteps)):
        x.append([times[i]] * df[timesteps[i]].shape[0])
    x = sum(x, [])
    x = np.array(x)

    y = []
    for i in range(len(lineage)):
        temp = []
        for j in range(len(timesteps)):
            ratios = df[timesteps[j]][lineage[i]] / df[timesteps[j]][lineage[0]] # element-wise division
            if bootstrap:
                # print("Bootstrapping...")
                ratios = np.random.choice(ratios, size=ratios.shape[0], replace=True)
            temp.append(ratios.tolist())
        temp = sum(temp, [])
        y.append(temp)
    y = np.array(y)
    y = y[1:] # Exclude LT-HSC (first parent species)
    y = y.flatten()

    try:
        assert int(y.shape[0] / x.shape[0]) == len(lineage) - 1
    except AssertionError:
        print("Internal error with data shapes... Exiting.")
        exit(1)
    return x, y