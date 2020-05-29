from .data import DataLoader, get_data_home, clear_data_home

from .data_redundancy import count_triplets, duplicates
from .data_redundancy import cartesian_product_relations

from .datasets import load_fb15k, load_fb13, load_fb15k237
from .datasets import load_wn18, load_wn18rr
from .datasets import load_yago3_10, load_wikidatasets

from .dissimilarities import l1_dissimilarity, l2_dissimilarity
from .dissimilarities import l1_torus_dissimilarity, l2_torus_dissimilarity, \
    el2_torus_dissimilarity

from .losses import MarginLoss, LogisticLoss
from .modelling import init_embedding, get_true_targets, load_embeddings
from .operations import get_rank, get_mask, get_bernoulli_probs
from .training import Trainer, TrainDataLoader
