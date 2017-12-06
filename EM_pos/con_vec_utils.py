__author__ = 'debjit'
'''modified esther's code'''

import utils as ut

"""
con to vec and back utils
"""

def uni_to_uni_num(uni, uni_set,column):
    inds = {}
    pre=[]
    pre=['AUX','CC','CD','DT','EX','FW','IN','JJ','JJ|DT','JJR','JJS','LS','MD','NN','NNP|JJ','NP','PP','NNS','NNP','NNPS','PDT','POS','PP$','PRP','PRP$','RB','RBR','RBS','RP','SYM','TO','UH','VB','VBD','VBG','VBG|NN','VBN','VBP','VBZ','WDT','WP','WP$','WRB','PRP|MD','sup/CD',':',')','(','.',',',"''",'``','$','#','--','-','\n', '{','}',"'"]
    pre=[pre[i].lower() for i in range(len(pre))]
    uni_set=pre
    for i in range(len(uni_set)):
        inds[uni_set[i]] = i  
    uni_num = []
    for i in range(len(uni)):
        
        uni_num.append(inds[uni[i]])
        
    return uni_num

def uni_num_to_uni(uni_num, labelset):
    pre=['AUX','CC','CD','DT','EX','FW','IN','JJ','JJ|DT','JJR','JJS','LS','MD','NN','NNP|JJ','NP','PP','NNS','NNP','NNPS','PDT','POS','PP$','PRP','PRP$','RB','RBR','RBS','RP','SYM','TO','UH','VB','VBD','VBG','VBG|NN','VBN','VBP','VBZ','WDT','WP','WP$','WRB','PRP|MD','sup/CD',':',')','(','.',',',"''",'``','$','#','--','-','\n', '{','}',"'"]
    pre=[pre[i].lower() for i in range(len(pre))]
    labelset=pre
    uni = [labelset[n] for n in uni_num]
    
    return uni

def load_conll(conll_path, delim='\t', est=False, y_column='c'):
    file = open(conll_path).readlines()
    
    if est:
        file = file[:]
        
    X = []
    Y = []
    vocabulary = []
    labels = []
    
    for l in file:     
        
        if len(l) == 1:
            sent_end_marker = l
            
            x = sent_end_marker
            y = sent_end_marker
        else:
            split_line = l.split(delim)
            x = split_line[0]
            
            if y_column == 'c':
              
                y = split_line[-1].strip('\n').strip()
                 
            elif y_column == 'z':
              
                y = split_line[-2].strip('\n').strip()
                
            else:
                print('From which column should I retrieve the labels? Column nr is', len(split_line))
        vocabulary.append(x)
        labels.append(y)
        X.append(x)
        Y.append(y)
        

    #labels = ut.get_labels()
    #print(labels)
    #pre=[]
    pre=['AUX','CC','CD','DT','EX','FW','IN','JJ','JJ|DT','JJR','JJS','LS','MD','NN','NNP|JJ','NP','PP','NNS','NNP','NNPS','PDT','POS','PP$','PRP','PRP$','RB','RBR','RBS','RP','SYM','TO','UH','VB','VBD','VBG','VBG|NN','VBN','VBP','VBZ','WDT','WP','WP$','WRB','PRP|MD','sup/CD',':',')','(','.',',',"''",'``','$','#','--','-','\n', '{','}',"'"]
    pre=[pre[i].lower() for i in range(len(pre))]
    labelset=pre
    labels = list(set(labels))
    
    #labels.pop(labels.index(sent_end_marker))
    
    #labels = labels + [sent_end_marker]
    vocabulary = list(set(vocabulary))
    
    return X, Y, vocabulary, labels

def uni_to_conll(x_uni, y_uni, orig=None):

    conlllines = []
    ineq = 0
    for i in range(len(x_uni)):
        conllline = x_uni[i] + '\t' + y_uni[i] + '\n'
        if orig:
            if orig[i] != y_uni[i]:
                #print(orig[i],'\t', y_uni[i],'\n')
                ineq += 1
            conllline = x_uni[i] + '\t' + orig[i] + '\t' + y_uni[i] + '\n'
        if x_uni[i] == '\n':
            conllline = x_uni[i]
        conlllines.append(conllline)
    print('Ineq:', ineq, 'Total', len(x_uni))

    return conlllines
