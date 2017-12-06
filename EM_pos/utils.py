__author__ = 'esthervandenberg'
'''modified esther's code'''

import numpy as np
#import noise_utils as nois
#import noise_injector as nois
import random

def random_select(P):
    # takes a sequence P of real positive numbers,
    # randomly selects an element p and return its index i

    # construct scale of classes
    accum_P = [P[0]]
    for i2 in range(1, len(P)):
        accum_P.append(accum_P[i2-1]+P[i2])

    # guess a number and find associated class
    i = random.uniform(0.01, .99)

    find_interval = list(accum_P)
    find_interval.append(i)
    find_interval.sort()

    i_idx = find_interval.index(i)
    right_bound = find_interval[i_idx+1]
    label = accum_P.index(right_bound)

    """
    print(accum_P)
    print(i)
    print(find_interval)
    print(i_idx)
    print(right_bound) ###
    print(label)
    """

    return label

###

def get_zt(labels):
    nr_instances = labels.shape[0]
    r=[]
    s=0
    for i in range(nr_instances):
         s=random.choice([j for j, x in enumerate(list(labels[i])) if x == max(list(labels[i]))])
         r.append(s)
    return r

def get_reverse_zt(c, start_from_0=True):
    nr_instances = len(c)
    nr_classes = max(c)+1
    reverse_zt = np.zeros([nr_instances, nr_classes])
    print(reverse_zt.shape)    
    for t in range(nr_instances):
        if start_from_0:
            labelind = c[t]
        else:
            labelind = c[t]-1
        reverse_zt[t,labelind] = 1        
    return reverse_zt

###
###

def dist(A, B):
    return abs(get_frob_norm(A) - get_frob_norm(B))

def get_frob_norm(A):
    return np.sqrt(np.trace(np.dot(np.transpose(A), A)))

###

##def make_uni_noisy(labels, p=0.1):
  ##  noisy_labels = nois.uni(labels, p=0.1)
  ##  return noisy_labels

###

def frac_from_lev(noise_level):
    frac = float(noise_level[0] + '.' + noise_level[1])
    return frac

def lev_from_frac(frac):
    # 0.00 to 000
    str_from_flt = str(frac)
    str_wo_dot = str_from_flt.replace('.', '')
    return str_wo_dot


###

def get_labels():
    content = open('/nethome/evdberg/NER_NoisyLabelNeuralNetwork/labels.txt').readlines()
    labels = [l.strip('\n') for l in content] + ['\n']
    #pre=[]
    #pre=['CC','CD','DT','EX','FW','IN','JJ','JJ|DT','JJR','JJS','LS','MD','NN','NP','PP','NNS','NNP','NNPS','PDT','POS','PP$','PRP','PRP$','RB','RBR','RBS','RP','SYM','TO','UH','VB','VBD','VBG','VBG|NN','VBN','VBP','VBZ','WDT','WP','WP$','WRB','PRP|MD','sup/CD',':',')','(','.',',',"''",'``','$','#','\n']
    labels=pre 
    return labels


def parse_type(type):
    ntype = type[3:6]
    if ntype == 'art':
        ntype = ''
    return type[:3], ntype, type[6:] # lang, ntype, lev
