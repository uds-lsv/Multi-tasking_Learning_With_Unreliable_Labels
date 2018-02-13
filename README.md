# Multi-tasking Learning With Unreliable Labels
This directory contains the following parts of the 'Multi-tasking Learning with un-reliable labels' experiment conducted for the MSc Thesis.
Extending the NLNN algorithm proposed by Bekker & Goldbergers in a Multi-tasking Learning set-up to handle noisy labels. 
In order to extend low-resource data we often used artificial annotators.
In this following setup we aim to generate clean training labeled data from artificial annotators. 

## Requirements 
~~~~
- python2.7 +

- Stanford-parser

- Senna - Neural network based tagger

- Brill Tagger- Rule-based tagger

- DyNet 
~~~~
## Pre-processing steps: 
- Sentence seperator using [stanford](https://nlp.stanford.edu/software/tokenizer.shtml) tool.  
- Then transfering the text into CONLL format.

## Tagging with Tagger:
- Tagging with Senna or Brill Tagger

## Post-processing step: 
- Sentence seperator after tagging the words  

### Data 
- Penn Treebank corpus (Human annotated labels) and North American Corpus (Artificially annotated)

### Neural Network Architecture 
- Low level supervised MTL (https://bitbucket.org/soegaard/mtl-cnn.git)

### Expectation and Maximization

- Python scripts with helper functions (utils.py + con_vec_utils.py) (Extended and modified the code by [Esther](https://github.com/EstherMaria/NoisyLabelNeuralNetwork))
- Python scripts for the EM noise distribution estimation module (singeEM.py + EM.py) (Extended and modified the code by [Esther](https://github.com/EstherMaria/NoisyLabelNeuralNetwork))

### Evaluation

- An evaluation script (prediction.py for Chunking and prediction_pos.py for POS) used [sckit-learn](http://scikit-learn.org/)

### Demo script

- demo_script.sh
- Python scripts with support functions (addpenntree\_chunk.py, addpenntree+NN\_chunk.py and addpenntree\_pos.py and addpenntree+NN\_pos.py) 


