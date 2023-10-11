from prepare_data import *

x, y = get_label_freq()
for i in range(int(y.shape[0] / x.shape[0])):
    plt.scatter(x, y[i*x.shape[0]:(i+1)*x.shape[0]])
plt.show()