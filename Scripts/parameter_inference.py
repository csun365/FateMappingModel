import sys
sys.path.insert(0, "Source")

from libraries import *
from constants import *
from curve_fitting import *
from prepare_data import *
from model_wrapper import *
from calculate_raw_counts import *

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--bootstrap", help="apply bootstrapping to the data (e.g. for confidence interval)")
parser.add_argument("--save", help="0 (False) or 1 (True) representing whether to save results (automatically 1 with boostrapping)")
cmdline_args = parser.parse_args()

num_bootstraps = None
if cmdline_args.bootstrap:
    num_bootstraps = int(cmdline_args.bootstrap)
save_bool = False
if cmdline_args.save:
    save_bool = bool(cmdline_args.save)

# Tau Calculation
taus, _ = run_model(num_bootstraps, save_output=save_bool)
taus_dict = {lineage[i + 1]: taus[i] for i in range(len(taus))}
print("\nTaus:")
print(taus_dict)

# Count Ratios Calculation
count_ratios_dict = {}
for key, value in lineage_dict.items():
    for reference_species in value:
        count_ratios_dict[reference_species] = compute_counts_ratio(reference_species, key, "mean")
print("\nCount Ratios:")
print(count_ratios_dict)

# Alpha Calculation
alpha_dict = {}
for key, value in lineage_dict.items():
    for reference_species in value:
        alpha_dict[reference_species] = 1 / taus_dict[reference_species] * count_ratios_dict[reference_species]
    
# Beta Calculation
beta_dict = {}
for key, value in lineage_dict.items():
    if key != lineage[0]:
        sum_alphas = 0
        for reference_species in value:
            sum_alphas += alpha_dict[reference_species]
        beta_dict[key] = sum_alphas - 1 / taus_dict[key]
beta_dict = {**{lineage[0]: list(alpha_dict.values())[0]}, **beta_dict}
print("\nAlphas:")
print(alpha_dict)
print("\nBetas:")
print(beta_dict)