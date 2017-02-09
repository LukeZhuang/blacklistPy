import numpy as np
import scipy.optimize as opt
import cost


def startTrain(trainx, trainy, lamb):
    m = trainx.shape[0]
    n = trainx.shape[1] + 1
    X = np.column_stack((np.ones((m, 1), dtype=float), trainx))
    y = trainy
    init_theta = np.zeros(n, dtype=float)
    theta = opt.fmin_cg(cost.costFunction, init_theta, fprime=cost.costFunctionGrad, args=(X, y, lamb))
    return theta


if __name__ == '__main__':
    # x = np.ones((3, 1), dtype=int)
    # print np.asarray(x)


    def f(x):
        a = x[0]
        b = x[1]
        return (a + b) ** 2 + 10


    def fGrad(x):
        a = x[0]
        b = x[1]
        return np.mat('%s;%s' % (2 * (a + b), 2 * (a + b)))


    init_x = np.mat('3;3').T
    print init_x
    print fGrad(init_x).T
    res = opt.fmin_cg(f, init_x, fprime=fGrad)
    print res
