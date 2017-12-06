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
    rec = recall_score(y_true, y_pred, labels=['b-np', 'b-pp', 'i-np', 'b-vp', 'i-vp', 'b-sbar', 'o', 'b-adjp', 'b-advp', 'i-advp', 'i-adjp', 'i-sbar', 'i-pp', 'b-prt', 'b-lst', 'b-intj', 'i-intj', 'b-conjp', 'i-conjp', 'i-prt', 'b-ucp', 'i-ucp','i-lst'],average='micro')
    print(rec)
    prec = precision_score(y_true, y_pred, labels=['b-np', 'b-pp', 'i-np', 'b-vp', 'i-vp', 'b-sbar', 'o', 'b-adjp', 'b-advp', 'i-advp', 'i-adjp', 'i-sbar', 'i-pp', 'b-prt', 'b-lst', 'b-intj', 'i-intj', 'b-conjp', 'i-conjp', 'i-prt', 'b-ucp', 'i-ucp','i-lst'],average='micro')
    print(prec)
    f1 = f1_score(y_true, y_pred,labels=['b-np', 'b-pp', 'i-np', 'b-vp', 'i-vp', 'b-sbar', 'o', 'b-adjp', 'b-advp', 'i-advp', 'i-adjp', 'i-sbar', 'i-pp', 'b-prt', 'b-lst', 'b-intj', 'i-intj', 'b-conjp', 'i-conjp', 'i-prt', 'b-ucp', 'i-ucp','i-lst'],average='micro')
    print(f1)
    conf_mat = confusion_matrix(y_true, y_pred,labels=['b-np', 'b-pp', 'i-np', 'b-vp', 'i-vp', 'b-sbar', 'o', 'b-adjp', 'b-advp', 'i-advp', 'i-adjp', 'i-sbar', 'i-pp', 'b-prt', 'b-lst', 'b-intj', 'i-intj', 'b-conjp', 'i-conjp', 'i-prt', 'b-ucp', 'i-ucp','i-lst'])
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
    

if __name__ == '__main__':
    main()
