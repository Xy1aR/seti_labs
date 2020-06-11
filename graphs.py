import random
import math
import matplotlib.pyplot as plt
import numpy as np


def graphMD_synch(l, M_D):
    fig, ax = plt.subplots()
    y = (2 - l) / (2 * (1 - l)) + 0.5
    y1 = M_D
    ax.plot(l, y, 'r-')
    ax.plot(l, y1, 'm-')
    plt.show()


def graphMD_asynch(l, M_Da):
    fig, ax = plt.subplots()
    y = (2 - l) / (2 * (1 - l))
    y1 = M_Da
    ax.plot(l, y, 'r-')
    ax.plot(l, y1, 'm-')
    plt.show()


def graphMN(l, M_N):
    fig, ax = plt.subplots()
    y = (l * (2 - l)) / (2 * (1 - l))
    y1 = M_N
    ax.plot(l, y, 'r-')
    ax.plot(l, y1, 'm-')
    plt.show()


def req_org(l, num_req):
    reqs = []
    q = 0
    i = 0
    while i < num_req:
        r = random.random()
        q = q - math.log(r) / l
        reqs.append(q)
        i += 1
    return reqs


def synch(reqs):
    num = len(reqs)
    d = []
    queue = []
    done_reqs = 0
    time = 0
    count = 0
    for i in range(num):
        queue.append(reqs[i])
    while done_reqs != num:
        if queue[0] < time:
            for i in range(len(queue)):
                if queue[i] < time:
                    count += 1
            time += 1
            done_reqs += 1
            d.append(time - queue[0])
            queue.pop(0)
        else:
            time += 1
    return (MD(d, len(reqs)), count / time)


def asynch(reqs):
    num = len(reqs)
    d = []
    queue = []
    done_reqs = 0
    time = 0
    for i in range(num):
        queue.append(reqs[i])
    while done_reqs != num:
        if queue[0] <= time:
            time += 1
            d.append(time - queue[0])
            queue.pop(0)
            done_reqs += 1
        else:
            time += 0.001
    return (MD(d, len(reqs)))


def MD(d, l):
    sum = 0
    for i in range(len(d)):
        sum += d[i]
    MD = sum / l
    return (MD)


l = np.linspace(0.01, 1, num=10, endpoint=False)
num_req = int(input("введите количество запросов: ", ))
M_D = []
M_N = []
M_Da = []
for i in range(len(l)):
    reqs = req_org(l[i], num_req)
    M_D.append(synch(reqs)[0])
    M_N.append(synch(reqs)[1])
    M_Da.append(asynch(reqs))
graphMD_synch(l, M_D)
graphMD_asynch(l, M_Da)
graphMN(l, M_N)
