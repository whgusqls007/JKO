import torch
from torch import nn
import numpy as np
from kobert.utils import get_tokenizer
import gluonnlp as nlp
from kobert.pytorch_kobert import get_pytorch_kobert_model
from torch.utils.data import Dataset
from torch.utils.data import dataloader

class BERTClassifier(nn.Module):

    def __init__(self,bert,hidden_size=768, num_classes=3, dr_rate=None, news_class=None,params=None):
        super(BERTClassifier, self).__init__()

        self.bert = bert
        self.dr_rate = dr_rate

        # 카테고리 별 label 수가 다름
        if news_class != 'society':
            num_classes = 3
        else:
            num_classes = 5

        self.classifier = nn.Linear(hidden_size, num_classes)
        if dr_rate:
            self.dropout = nn.Dropout(p=dr_rate)

    def gen_attention_mask(self, token_ids, valid_length):
        attention_mask = torch.zeros_like(token_ids)
        for i, v in enumerate(valid_length):
            attention_mask[i][:v] = 1
        return attention_mask.float()

    def forward(self, token_ids, valid_length, segment_ids):
        attention_mask = self.gen_attention_mask(token_ids, valid_length)

        _, pooler = self.bert(input_ids=token_ids, token_type_ids=segment_ids.long(),
                              attention_mask=attention_mask.float().to(token_ids.device))
        if self.dr_rate:
            out = self.dropout(pooler)
        return self.classifier(out)