import numpy as np
import sigmoid as sig


def costFunction(theta, X, y, lamb):
    theta = np.mat(theta).T
    m = X.shape[0]
    h = sig.sigmoidFunction(X, theta)
    # print h
    J = -(1. / m) * (y.T * np.log(h + 1e-10) + (1 - y).T * np.log(1. - h + 1e-10)) + (lamb / 2 / m) * np.sum(
        np.power(theta[1:, :], 2))
    return J


def costFunctionGrad(theta, X, y, lamb):
    theta = np.mat(theta).T
    m = X.shape[0]
    h = sig.sigmoidFunction(X, theta)
    temp = lamb * theta
    temp[0, 0] = 0
    grad = (1. / m) * (X.T * (h - y) + temp)
    return np.array(grad.T.tolist()[0])


if __name__ == '__main__':
    # import scipy.optimize as opt
    #
    #
    # def f(x, y, z):
    #     return (x + y) ** 2 + z
    #
    #
    # def fGrad(x, y, z):
    #     return 2 * (x + y)
    #
    #
    # res = opt.fmin_cg(f, 10, fprime=fGrad, args=(5, 3))
    # print res
    # x = np.mat('3;3;3')
    # y = np.column_stack((np.mat('2;2;2'), x))
    # print y
    # print np.sum(x)
    # print np.sum(np.power(x, 2))
    x = np.mat('1,2,3')
    print x.tolist()[0]
