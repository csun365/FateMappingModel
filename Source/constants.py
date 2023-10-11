from import_data import *

data = get_data("label")

# Qualitative description of when data is collected
timesteps = list(data.keys())

# Stem cell differentiation pathway 
lineage = list(data[list(data.keys())[0]].columns)

# Month to days
month_to_days = 30.436875

# Numerical representation of timesteps
times = [7] + [float(timesteps[i][:2]) * month_to_days for i in range(1, len(timesteps))]