__author__ = 'debjit'
'''modified esther's code'''
import argparse as ap
from EM import EMModule
import numpy as np
import con_vec_utils as ctv
import utils as ut
import os
if __name__ == "__main__":
    parser = ap.ArgumentParser(description='Singe EM iteration', usage='SingleEM_no_noise [-initialize] [-true_theta][-file] ')
    parser.add_argument("-file", help=".txt file containing the input text", nargs='?')
    parser.add_argument('-type', help="Give percentage of noise")
    parser.add_argument('-initialize', help="to initialize with pre-saved estimated labels from pre-trained model", action="store_true")
    parser.add_argument('-true_theta', help="to load pre-saved theta into EMModule", action="store_true")
    parser.add_argument('-tracking', help="verbose mode", action="store_true")
    args = parser.parse_args()
# retrieve predictions & convert to vector
    estlab_path = args.file #"/data/users/dpaul/Thesis/Practical/Data/Data_North_Clean/Output_trail_train/original_20000_out"
    est_x_uni, est_y_uni, est_vocabulary, est_labels  = ctv.load_conll(estlab_path, delim='\t', est=True, y_column='c')
    est_labels = est_labels #ut.get_labels() 
    est_y_num = ctv.uni_to_uni_num(est_y_uni, est_labels,'c')
    est_y_vector = ut.get_reverse_zt(est_y_num)
# retrieve original old labels & convert to vector
    noisy_x_uni, noisy_y_uni, noisy_vocabulary, noisy_labels  = ctv.load_conll(estlab_path, delim='\t', est=True, y_column='z')  
    #noisy_labels= pre  
    noisy_y_num = ctv.uni_to_uni_num(noisy_y_uni, noisy_labels,'z')    
    noisy_y_vector = ut.get_reverse_zt(noisy_y_num) 
   
    if args.tracking:
        print("tracking progress to vector")
        print('nr instances should be', len(est_x_uni))
        print('nr labels should be', len(est_labels), est_labels)
        print('original estimated labels labelset was:', pre)
        if len(est_x_uni) != len(noisy_x_uni):
            print('Nr instances not the same')
        elif max(est_y_num) != max(noisy_y_num):
            print('Nr labels not the same')
        print('Shapes of vectors are: ', np.shape(est_y_vector), np.shape(noisy_y_vector))
    z = noisy_y_vector    
    prob_y = est_y_vector         
    print('Getting Estlabs from: ',estlab_path, 'Difference Estlab (prob_y) and orig (z):', ut.dist(z, prob_y))#+ '/' + estlab_path
# retrieve or initialize theta
    if args.initialize:
        EM = EMModule(initialize=True, initializer=prob_y, labels=z)
        print(EM.theta)
        np.save('/data/users/dpaul/Thesis/Practical/My_code/Debjit_Code/theta/theta'+args.type, EM.theta) 
        print('Saved initialised theta to','/data/users/dpaul/Thesis/Practical/My_code/Debjit_Code/theta'+'/theta'+ args.type+'.npy')
    elif args.true_theta:
        EM = EMModule(labels=z)
        EM.theta = np.load('./theta' + '.npy')
        print('Loaded true theta from', os.getcwd() + '/truethetas'+'/theta'+ args.type + '.npy')
        print(EM.theta)
    else:
        EM = EMModule(labels=z)
        EM.theta = np.load('/data/users/dpaul/Thesis/Practical/My_code/Debjit_Code/theta/theta'+ args.type +'.npy') #/nethome/evdberg/NER_NoisyLabelNeuralNetwork/   ### temporary my change
        
        print('Loaded theta from','/data/users/dpaul/Thesis/Practical/My_code/Debjit_Code/theta/theta'+ args.type +'.npy')
        print(EM.theta)
    prev_theta = EM.theta
# iterates once, gets improved theta, updates and checks for convergence
    print("Updating theta and c")
           
    c_vector, new_theta = EM.iteration(prob_y)
    print('theta after iteration:', new_theta)
    # save c and theta
    if not args.true_theta:
        np.save('/data/users/dpaul/Thesis/Practical/My_code/Debjit_Code/theta/theta', new_theta) #/nethome/evdberg/NER_NoisyLabelNeuralNetwork/  ### temporary my change new_theta 
    c_num = ut.get_zt(c_vector)    
    c_uni = ctv.uni_num_to_uni(c_num, est_labels)
    #print(c_uni)
    if args.true_theta:
        output_path = estlab_path+'_true'
        c_conll = ctv.uni_to_conll(est_x_uni, c_uni) #without pred xc, with pred xyc
        with open(output_path, 'w') as f:
            for out_line in c_conll:
                f.write(out_line)
            print('Wrote to', output_path)
    elif args.initialize:
        c_conll_xyc = ctv.uni_to_conll(est_x_uni, c_uni, orig=noisy_y_uni) #without pred xc, with pred xyc
        output_xyc = estlab_path
        
        with open(output_xyc, 'w') as f:
            for out_line in c_conll_xyc:               
                f.write(out_line)
            print('Wrote updates estlab (c) to: ', output_xyc)
        c_conll_xc = ctv.uni_to_conll(est_x_uni, c_uni) #without pred xc, with pred xyc
        output_xc = estlab_path+'_update'
        with open(output_xc, 'w') as f:
            for out_line in c_conll_xc:
                f.write(out_line)

    else:             
        c_conll_xyc = ctv.uni_to_conll(est_x_uni, c_uni, orig=noisy_y_uni) #without pred xc, with pred xyc
        output_xyc = estlab_path
        
        with open(output_xyc, 'w') as f:
            for out_line in c_conll_xyc:               
                f.write(out_line)
            print('Wrote updates estlab (c) to: ', output_xyc)
        c_conll_xc = ctv.uni_to_conll(est_x_uni, c_uni) #without pred xc, with pred xyc
        output_xc = estlab_path+'_update'
        with open(output_xc, 'w') as f:
            for out_line in c_conll_xc:
                f.write(out_line)
