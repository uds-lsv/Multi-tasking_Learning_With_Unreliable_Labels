#!/usr/bin/env python3
#adding clean data after every EM step
import os
import argparse
import random
import ntpath
import sys
import itertools
import re

def read_pos_tree_file(data):
    if data is None:
        file = sys.stdin
    else:
        file = open(data,'r')
    graph = []
    clean_graph=[]    
    lines=file.readlines()
    file1= open('/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/Noise_free.pos_clean','r')
    content=file1.readlines()
    file2= open(data+'_mix','w')
    n=0
    for line in content:   
       n=n+1
       if n <=904383:
           file2.write(line)  
       else:
           n=n
                         
    file2.close()
    file2= open(data+'_mix','a')
    n=0
    for line in lines:   
       n=n+1
       if n>904383:
           file2.write(line)                       
    file2.close()
    return 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("posfile", help=".pos file containing the input text", nargs='?')
    #parser.add_argument("file", help=".pos file containing the input text", nargs='?')
    args = parser.parse_args()
    read_pos_tree_file(args.posfile)
    


if __name__ == '__main__':
    main()
