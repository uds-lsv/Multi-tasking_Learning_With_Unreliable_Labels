__author__ = 'debjit'

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import sys
import os
import argparse
import random
import ntpath
import itertools
import re

def get_prec_red_f1_conf(xyc_path):
    y_true = []
    y_pred = []
    with open(xyc_path)as f:
        lines = f.readlines()[:]
        for l in lines:
           if l!='\n':
            spline = l.split('\t') 
            y_true.append(spline[1].strip())
            y_pred.append(spline[2].strip('\n'))   
    acc = accuracy_score(y_true, y_pred)
    print(acc)
    pre=['AUX','AUXG','CC','CD','DT','EX','FW','IN','JJ','JJ|DT','JJR','JJS','LS','MD','NN','NP','PP','NNS','NNP','NNPS','PDT','POS','PP$','PRP','PRP$','RB','RBR','RBS','RP','SYM','TO','UH','VB','VBD','VBG','VBG|NN','VBN','VBP','VBZ','WDT','WP','WP$','WRB','PRP|MD',':',')','(','.',',',"''",'``','$','#','\n']
    pre=[pre[i].lower() for i in range(len(pre))]
    rec = recall_score(y_true, y_pred, labels=pre,average='micro')
    print(rec)
    prec = precision_score(y_true, y_pred, labels=pre,average='micro')
    print(prec)
    f1 = f1_score(y_true, y_pred,labels=pre,average='micro')
    print(f1)
    conf_mat = confusion_matrix(y_true, y_pred,labels=pre)
    metrics = [acc, prec, rec, f1]
    m_new = ["%.2f" % (m*100) for m in metrics]
    print(tuple([float(m) for m in m_new]))
    print(' & '.join(m_new) + " \\\\")
    return 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-file", help=".pos file containing the input text", nargs='?')
    args = parser.parse_args()
    get_prec_red_f1_conf(args.file)
    ##newgraph, V, E = perform_BFS(graph, V, E, args.center, args.radius)


if __name__ == '__main__':
    main()
