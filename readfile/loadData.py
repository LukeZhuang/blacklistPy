import random as rand
import numpy as np

def load_data():
    fx = open('datax.csv')
    fy = open('datay.csv')
    data = []
    datay = []
    for line in fx:
        cols = line.split(',')
        data.append([cols[0], cols[1], cols[2][:-1]])
    for line in fy:
        cols = line.split(',')
        datay.append((cols[0][:-1]))
    for i in range(len(data)):
        data[i].append(datay[i])
    rand.shuffle(data)
    m = len(data)
    trainx = np.mat('0,0,0')
    trainy = np.mat('0')
    testx = np.mat('0,0,0')
    testy = np.mat('0')
    for i in range(int(m * 0.7)):
        trainx = np.row_stack((trainx, np.mat('%s, %s, %s' % (data[i][0], data[i][1], data[i][2]))))
        trainy = np.row_stack((trainy, np.mat('%s' % (data[i][3]))))
    for i in range(int(m * 0.7), m):
        testx = np.row_stack((testx, np.mat('%s, %s, %s' % (data[i][0], data[i][1], data[i][2]))))
        testy = np.row_stack((testy, np.mat('%s' % (data[i][3]))))
    trainx = trainx[1:, :]
    trainy = trainy[1:, :]
    testx = testx[1:, :]
    testy = testy[1:, :]
    return 1.*trainx, 1.*trainy, 1.*testx, 1.*testy


if __name__ == '__main__':
    pass