from libraries import *

def get_data(mode):
    # Mode is a string: either "label" or "raw"
    root = "Data/"
    ls = os.listdir(root)
    path = [i for i in ls if i.startswith(mode)][0]
    return pd.read_excel(root + path, sheet_name=None)
