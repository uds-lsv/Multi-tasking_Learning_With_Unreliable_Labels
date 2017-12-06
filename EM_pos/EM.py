__author__ = 'Esther and extended by Debjit'
"""
This class EMModule initialises a noise distribution (theta) and estimated labels (c) based on observed labels and
NN predictions. EM Iterations then improve theta and c and update the NN accordingly to get better predictions.
We added an smoothing function while estimating the new labels.
"""

import numpy as np
import utils as ut
class EMModule:
    def __init__(self, initialize=False, initializer=None, labels=None):
        self.initializer = initializer
        self.labels = labels
        self.nr_classes = labels.shape[1]
        self.nr_instances = labels.shape[0]
        if initialize:
            self.theta = self.get_theta(initializer, labels)
        self.zt = ut.get_zt(self.labels)
        self.c = np.zeros([self.nr_instances, self.nr_classes])
    def get_theta(self, c, z):
        theta = np.zeros([self.nr_classes] * 2)
        denoms = np.sum(c, axis=0)
        nums = np.dot(np.transpose(c), z)
        for i in range(self.nr_classes):
            for j in range(self.nr_classes):
                if denoms[i] == 0.0:
                    theta[i,j] = 0
                else:
                    theta[i,j] = nums[i,j] / denoms[i]
        return theta
    def iteration(self, new_prob_y):
        prev_theta = self.theta
        # update c
        denoms_c = np.transpose(np.dot(np.transpose(prev_theta), np.transpose(new_prob_y)))
        for t in range(self.nr_instances):
            for i in range(self.nr_classes):
                num_c = prev_theta[i,self.zt[t]] * new_prob_y[t,i]
                self.c[t,i] = (num_c + 0.00000001) / (denoms_c[t, self.zt[t]]+(self.nr_classes*0.00000001))
        print('Theta has shape:', np.shape(prev_theta), 'Difference new estlab (c) and orig estlab (prob_y):', ut.dist(new_prob_y, self.c)) #self.nr_instances, self.nr_classes
        # update theta
        self.theta = self.get_theta(self.c, self.labels)
        print('Returned updated parameters...')
        return self.c, self.theta
