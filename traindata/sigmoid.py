import numpy as np

def sigmoidFunction(x,theta):
    return 1/(1+np.exp(-x*theta))

if __name__ == '__main__':
    pass
