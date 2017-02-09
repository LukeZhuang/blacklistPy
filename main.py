import numpy as np
import readfile.loadData as ld
import traindata.train as train
import performance.perform as perf
import matplotlib.pyplot as plot

(trainx, trainy, testx, testy) = ld.load_data()
theta = train.startTrain(trainx, trainy, 1.0)
alpha_list = np.linspace(0, 1, 101)
ks = -1.0
max_alpha = -1.0
plot.figure(1)
for alpha in alpha_list:
    (TPR, FNR) = perf.calcPerformance(testx, testy, np.mat(theta).T, alpha)
    temp = TPR - FNR
    # print (temp, TPR, FNR, alpha)
    plot.plot(FNR, TPR, '+')
    if temp > ks:
        ks = temp
        max_alpha = alpha
print '\nmaxium ks = %f where alpha = %f' % (ks, max_alpha)
plot.show()
