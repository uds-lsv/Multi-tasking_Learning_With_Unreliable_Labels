#!/bin/bash
#!export CUDA_ROOT=/usr/local/cuda-8.0
PYTHON=/nethome/dpaul/project1/bin/python2.7
OUTTEST=/data/users/dpaul/Thesis/Practical/Output/Test/Noise50_out
OUTTRAIN=/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out
INTRAIN=/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/50.cfg
INTEST=/data/users/dpaul/Thesis/Practical/wsj/chunk/sec_23
MODEL=/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.pos.best_model
MODEL_chunk=/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.chunk.best_model
MTL=/data/users/dpaul/Thesis/Practical/mtl-cnn/mtl_tagger1.py
ACCURACY=/data/users/dpaul/Thesis/Practical/My_code/Debjit_Code/prediction.py
ACCURACY_pos=/data/users/dpaul/Thesis/Practical/My_code/Debjit_Code/prediction_pos.py
F1SCORE=/data/users/dpaul/Thesis/Practical/mtl-cnn/fscore.py
EM=/data/users/dpaul/Thesis/Practical/My_code/Debjit_Code/SingleEM.py
EM_chunk=/data/users/dpaul/Thesis/Practical/EM_chunk/SingleEM.py
INTRAIN_MTL=/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/50_mtl.cfg
SPACE=/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/space.py
NEW_TAG=/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/new_tags.py
Add_data_pos=/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/addpenntree_pos.py
Add_data_NN_pos=/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/addpenntree+NN_pos.py
Add_data_chunk=/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/addpenntree_chunk.py
Add_data_NN_chunk=/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/addpenntree+NN_chunk.py
Embeds=/data/users/dpaul/Thesis/Practical/Download_Code/bilstm-aux-master/embeds/poly_a/en.polyglot.txt
ITER=0
MAXITER=10	
	
echo '' && echo 'Pre-training';	
$PYTHON $MTL --cfg $INTRAIN --out $OUTTRAIN --iters 10  --birnn --embeds $Embeds --in_dim 64 

echo '' && echo 'TEST';
$PYTHON $MTL TEST --model /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.chunk.best_model --test chunk:/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/Full.chunk.data
$PYTHON $MTL TEST --model /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.pos.best_model --test pos:/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/Full.pos.data

echo '' && echo 'CLEAN';
$PYTHON $SPACE out.pos.best_model.test.tagged.pos
$PYTHON $SPACE out.chunk.best_model.test.tagged.chunk

echo '' && echo 'Accuracy_Train POS';
$PYTHON $ACCURACY_pos -file /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.pos.best_model.test.tagged.pos_space

echo '' && echo 'Accuracy_Train CHUNK';
$PYTHON $ACCURACY -file /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.chunk.best_model.test.tagged.chunk_space

echo '' && echo 'Add_clean data';
$PYTHON $Add_data_pos /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.pos.best_model.test.tagged.pos_space
$PYTHON $Add_data_chunk /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.chunk.best_model.test.tagged.chunk_space

echo '' && echo 'Initializing theta POS';
$PYTHON $EM -file /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/Full.pos.data.train -initialize -type mtl_pos_50

echo '' && echo 'Initializing theta CHUNK';
$PYTHON $EM_chunk -file /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/Full.chunk.data.train -initialize -type mtl_chunk_50

echo '' && echo 'Accuracy_test_POS';
$PYTHON $MTL TEST --model /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.pos.best_model --test pos:/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/test.pos_temp
$PYTHON $ACCURACY_pos -file /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.pos.best_model.test.tagged.pos

echo '' && echo 'Accuracy_test_Chunk';
$PYTHON $MTL TEST --model /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.chunk.best_model --test chunk:/data/users/dpaul/Thesis/Practical/wsj/chunk/sec_20
$PYTHON $ACCURACY -file /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.chunk.best_model.test.tagged.chunk

echo '' && echo 'Add clean data';
$PYTHON $Add_data_NN_pos /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/Full.pos.data.train_update
$PYTHON $Add_data_NN_chunk /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/Full.chunk.data.train_update


while [ "$ITER" -lt "$MAXITER" ];
do echo $ITER;
ITER=$((ITER+1)); 

$PYTHON $MTL --cfg $INTRAIN_MTL --out $OUTTRAIN --iters 10 --birnn --embeds $Embeds --in_dim 64 

echo '' && echo 'TEST';
$PYTHON $MTL TEST --model /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.chunk.best_model --test chunk:/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/Full.chunk.data.train_update_mix
$PYTHON $MTL TEST --model /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.pos.best_model --test pos:/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/Full.pos.data.train_update_mix

echo '' && echo 'CLEAN';
$PYTHON $SPACE out.pos.best_model.test.tagged.pos
$PYTHON $SPACE out.chunk.best_model.test.tagged.chunk

echo '' && echo 'Accuracy_Train POS';
$PYTHON $ACCURACY_pos -file /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.pos.best_model.test.tagged.pos_space

echo '' && echo 'Accuracy_Train CHUNK';
$PYTHON $ACCURACY -file /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.chunk.best_model.test.tagged.chunk_space

echo '' && echo 'Add_clean data';
$PYTHON $Add_data_pos /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.pos.best_model.test.tagged.pos_space
$PYTHON $Add_data_chunk /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.chunk.best_model.test.tagged.chunk_space

echo '' && echo 'Updating theta POS';
$PYTHON $EM -file /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/Full.pos.data.train -initialize -type mtl_pos_50

echo '' && echo 'Updating theta CHUNK';
$PYTHON $EM_chunk -file /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/Full.chunk.data.train -initialize -type mtl_chunk_50

echo '' && echo 'Accuracy_test_POS';
$PYTHON $MTL TEST --model /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.pos.best_model --test pos:/data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/test.pos_temp
$PYTHON $ACCURACY_pos -file /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.pos.best_model.test.tagged.pos

echo '' && echo 'Accuracy_test_Chunk';
$PYTHON $MTL TEST --model /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.chunk.best_model --test chunk:/data/users/dpaul/Thesis/Practical/wsj/chunk/sec_20
$PYTHON $ACCURACY -file /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/out.chunk.best_model.test.tagged.chunk

echo '' && echo 'Add clean data';
$PYTHON $Add_data_NN_pos /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/Full.pos.data.train_update
$PYTHON $Add_data_NN_chunk /data/users/dpaul/Thesis/Practical/mtl_chunk_pos/50_noise/Full.chunk.data.train_update


done
