
# Multi-tasking Learning With Unreliable Labels (NAACL-SRW 2019)
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

## Reference

If you make use of the contents of this repository, please cite [the following paper](https://arxiv.org/abs/1904.00676):

```
@inproceedings{paul-etal-2019-handling,
    title = "Handling Noisy Labels for Robustly Learning from Self-Training Data for Low-Resource Sequence Labeling",
    author = "Paul, Debjit  and
      Singh, Mittul  and
      Hedderich, Michael A.  and
      Klakow, Dietrich",
    booktitle = "Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Student Research Workshop",
    month = jun,
    year = "2019",
    address = "Minneapolis, Minnesota",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/N19-3005",
    pages = "29--34",
    abstract = "In this paper, we address the problem of effectively self-training neural networks in a low-resource setting. Self-training is frequently used to automatically increase the amount of training data. However, in a low-resource scenario, it is less effective due to unreliable annotations created using self-labeling of unlabeled data. We propose to combine self-training with noise handling on the self-labeled data. Directly estimating noise on the combined clean training set and self-labeled data can lead to corruption of the clean data and hence, performs worse. Thus, we propose the Clean and Noisy Label Neural Network which trains on clean and noisy self-labeled data simultaneously by explicitly modelling clean and noisy labels separately. In our experiments on Chunking and NER, this approach performs more robustly than the baselines. Complementary to this explicit approach, noise can also be handled implicitly with the help of an auxiliary learning task. To such a complementary approach, our method is more beneficial than other baseline methods and together provides the best performance overall.",
}


