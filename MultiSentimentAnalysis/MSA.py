import torch
import numpy as np
from kobert.utils import get_tokenizer
import gluonnlp as nlp
from kobert.pytorch_kobert import get_pytorch_kobert_model
from torch.utils.data import dataloader
from BERTClassifier import BERTClassifier
from BERTDataset import BERTDataset
from predictFunctions import predictFunctions
from updateFunctions import updateFunctions

if __name__ == "__main__":


    UF = updateFunctions()
    UF.update('society')
    UF.update('sports')
    UF.update('economy')


    '''
    PF = predictFunctions()
    PF.predict_society('"처녀가 없다" 성희롱·지역 비하 발언 해경 경무관 강등')
    '''

