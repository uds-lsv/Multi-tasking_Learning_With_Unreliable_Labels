#!/usr/bin/env python3
#Adding clean data after every EM step
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
    pos_tags=[]
    words=[]   
    lines=file.readlines()
    file1= open('/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/Noise_free.chunk_clean','r')
    content=file1.readlines()
    file2= open('/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/Full.chunk.data.train','w')
    n=0
    for line in content:   
       n=n+1
       if n <=220663:
           if line =='\n':
              file2.write(line) 
           else: 
            words=str(line).rsplit('\t')[0].strip('\n')
            #line=line.rsplit(' ',1)[0] 
            pos_tags=str(line).rsplit('\t')[-1].strip('\n')
            
            s=str(words)+'\t'+str(pos_tags.lower())+'\t'+str(pos_tags.lower())+'\n'
            file2.write(s)
              
            
       else:
           n=n
                         
    file2.close()
    file2= open('/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/Full.chunk.data.train','a')
    n=0
    file1= open(data,'r')
    for line in lines:   
       n=n+1
       if n>220663:
           file2.write(line)                       
    file2.close()
    return 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("posfile", help=".pos file containing the input text", nargs='?')
    args = parser.parse_args()
    read_pos_tree_file(args.posfile)
    


if __name__ == '__main__':
    main()
