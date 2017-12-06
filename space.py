#python script to clean the ouput of MTL-NN 
#!/usr/bin/env python3
import glob
import os
import subprocess
import sys
import argparse

def read_file(data):
    graph = []
    clean_graph=[]
    n=0
    a=0
    words=[]
    space=[]
    chunk_tags=[]
    count=0
    flag=0
    pos_tags=[]
    new_pos_tags=[]
    print("Creating : /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/"+str(data)+str('_space'))
    file1=open("/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/"+str(data)+str('_space'),"w")
    file2=open("/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/"+str(data),"r") 
    lines=file2.readlines()
    for line in lines: 
        if line == '\n' and flag==0:
            file1.write('\n')
            flag=1
        elif line=='\n' and flag==1:
             flag=1    
        else:
            flag=0
            words=str(line).rsplit('\t')[0].strip('\n')
            #line=line.rsplit(' ',1)[0] 
            pos_tags=str(line).rsplit('\t')[1].strip('\n')
            new_pos_tags=str(line).rsplit('\t')[-1].strip('\n')
            s=str(words)+'\t'+str(pos_tags.lower())+'\t'+str(new_pos_tags.lower())+'\n'
            file1.write(s)
            
            
            
    
    return
 	

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("txtfile", help=".txt file containing the input text", nargs='?')
    args = parser.parse_args()
    read_file(args.txtfile)
    #print(args.txtfile)
     ##newgraph, V, E = perform_BFS(graph, V, E, args.center, args.radius)


if __name__ == '__main__':
    main()


   
            
