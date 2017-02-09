import numpy as np
import traindata.sigmoid as sig


def calcPerformance(X, y, theta, alpha):
    m = X.shape[0]
    n = X.shape[1] + 1
    X = np.column_stack((np.ones((m, 1), dtype=float), X))
    h = sig.sigmoidFunction(X, theta)
    TPR_num = 0
    FNR_num = 0
    tot_true = 0
    tot_false = 0
    for i in range(h.shape[0]):
        if int(y[i] == 1):
            tot_true += 1
        if int(y[i] == 0):
            tot_false += 1
        if h[i] >= alpha and int(y[i] == 1):
            TPR_num += 1
        if h[i] < alpha and int(y[i] == 0):
            FNR_num += 1
    return 1. * TPR_num / tot_true, 1. - 1. * FNR_num / tot_false


if __name__ == '__main__':
    x = np.array([1, 3, 2])
    for i in range(x.shape[0]):
        x[i] = int(x[i] > 1)
    print x
