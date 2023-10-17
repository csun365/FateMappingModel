from import_data import *

data = get_data("label")

# Qualitative description of when data is collected
timesteps = list(data.keys())

# Stem cell differentiation pathway 
lineage = list(data[list(data.keys())[0]].columns)

# Dictionary of upstream: reference pairs
lineage_dict = {"LT-HSC": ["ST-HSC"],
                "ST-HSC": ["MPP"],
                "MPP": ["CLP", "CMP"],
                "CMP": ["GMP", "MEP"],
                "CLP": ["proB", "DNT"],
                "proB": ["B cells"],
                "DNT": ["DPT"],
                "DPT": ["CD4+T", "CD8+T"]}

# Includes all species whose reference species is defined in the model
beta_upstream_lineage = ["ST-HSC", "MPP", "CLP", "CMP", "proB", "DNT", "DPT",]

# Month to days
month_to_days = 30.436875

# Numerical representation of timesteps
times = [7] + [float(timesteps[i][:2]) * month_to_days for i in range(1, len(timesteps))]