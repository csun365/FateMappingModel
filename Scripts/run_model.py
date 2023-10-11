import sys
sys.path.insert(0, "Source")
import warnings

from libraries import *
from constants import *
from curve_fitting import *
from prepare_data import *

# https://docs.python.org/3/howto/argparse.html
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--bootstrap", help="apply bootstrapping to the data (e.g. for confidence interval)")
cmdline_args = parser.parse_args()
# ---------------------------------------------

bootstrap = None
if cmdline_args.bootstrap:
    bootstrap = int(cmdline_args.bootstrap)

if bootstrap is None:
    x, y = get_label_freq(bootstrap=False)
    taus, tau_cov = curve_fit(growth_function, x, y, p0=[100] * int(y.shape[0] / x.shape[0]))
    pd.DataFrame(data=taus.reshape(1,-1), columns=lineage[1:]).to_csv("Results/tau_results.csv")
    np.save("Results/tau_cov.npy", tau_cov)
    print("\nModel terminated successfully.\n")
else:
    taus_list = []
    tau_cov_list = []
    for i in range(bootstrap):
        x, y = get_label_freq(bootstrap=True)
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore")
            taus, tau_cov = curve_fit(growth_function, x, y, p0=[100] * int(y.shape[0] / x.shape[0]))
        taus_list.append(taus)
        tau_cov_list.append(tau_cov)
        if (i + 1) % 10 == 0:
            print(f"Finished {i+1} bootstraps...")
            pd.DataFrame(data=np.array(taus_list), columns=lineage[1:]).to_csv(f"Results/tau_results_bootstrap_{bootstrap}.csv")
            np.save(f"Results/tau_cov_bootstrap_{bootstrap}.npy", np.array(tau_cov_list))
    print("\nModel terminated successfully.\n")