import torch
from torch import nn
import numpy as np
from kobert.utils import get_tokenizer
import gluonnlp as nlp
from kobert.pytorch_kobert import get_pytorch_kobert_model
from torch.utils.data import Dataset
from torch.utils.data import dataloader
from BERTClassifier import BERTClassifier
from BERTDataset import BERTDataset

class predictFunctions:

    def __init__(self):

        self.device = torch.device("cuda:0")
        self.bertmodel, self.vocab = get_pytorch_kobert_model()

        bertmodel, vocab = get_pytorch_kobert_model()

        # 토큰화
        tokenizer = get_tokenizer()
        self.tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)

        self.max_len = 64
        self.batch_size = 64

    def predict(self, predict_sentence, news_class):

        if news_class == 'society':
            return self.predict_society(predict_sentence)

        elif news_class == 'sports':
            return self.predict_sports(predict_sentence)

        elif news_class == 'economy':
            return self.predict_economy(predict_sentence)


    def predict_society(self, predict_sentence):

        model = BERTClassifier(self.bertmodel, dr_rate=0.5, news_class='society').to(self.device)
        model = torch.load('./model/society_model.pt')
        model.eval()

        data = [predict_sentence, '0']
        dataset_another = [data]

        another_test = BERTDataset(dataset_another, 0, 1, self.tok, self.max_len, True, False)
        test_dataloader = dataloader.DataLoader(another_test, batch_size=self.batch_size, num_workers=2)

        model.eval()

        for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_dataloader):
            token_ids = token_ids.long().to(self.device)
            segment_ids = segment_ids.long().to(self.device)

            valid_length = valid_length
            label = label.long().to(self.device)

            out = model(token_ids, valid_length, segment_ids)

            test_eval = []
            for i in out:
                logits = i
                logits = logits.detach().cpu().numpy()

                if np.argmax(logits) == 0:
                    return ('따뜻한')
                elif np.argmax(logits) == 1:
                    return ('신기한')
                elif np.argmax(logits) == 2:
                    return ('충격적인')
                elif np.argmax(logits) == 3:
                    return ('슬픈')
                elif np.argmax(logits) == 4:
                    return ('중립')

    def predict_sports(self, predict_sentence):

        model = BERTClassifier(self.bertmodel, dr_rate=0.5, news_class='sports').to(self.device)
        model = torch.load('./model/sports_model.pt')
        model.eval()

        data = [predict_sentence, '0']
        dataset_another = [data]

        another_test = BERTDataset(dataset_another, 0, 1, self.tok, self.max_len, True, False)
        test_dataloader = dataloader.DataLoader(another_test, batch_size=self.batch_size, num_workers=2)

        model.eval()

        for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_dataloader):
            token_ids = token_ids.long().to(self.device)
            segment_ids = segment_ids.long().to(self.device)

            valid_length = valid_length
            label = label.long().to(self.device)

            out = model(token_ids, valid_length, segment_ids)

            test_eval = []
            for i in out:
                logits = i
                logits = logits.detach().cpu().numpy()

                if np.argmax(logits) == 0:
                    return ('부정')
                elif np.argmax(logits) == 1:
                    return ('긍정')
                elif np.argmax(logits) == 2:
                    return ('중립')

    def predict_economy(self, predict_sentence):

        model = BERTClassifier(self.bertmodel, dr_rate=0.5, news_class='economy').to(self.device)
        model = torch.load('./model/economy_model.pt')
        model.eval()

        data = [predict_sentence, '0']
        dataset_another = [data]

        another_test = BERTDataset(dataset_another, 0, 1, self.tok, self.max_len, True, False)
        test_dataloader = dataloader.DataLoader(another_test, batch_size=self.batch_size, num_workers=2)

        model.eval()

        for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_dataloader):
            token_ids = token_ids.long().to(self.device)
            segment_ids = segment_ids.long().to(self.device)

            valid_length = valid_length
            label = label.long().to(self.device)

            out = model(token_ids, valid_length, segment_ids)

            test_eval = []
            for i in out:
                logits = i
                logits = logits.detach().cpu().numpy()

                if np.argmax(logits) == 0:
                    return ('부정')
                elif np.argmax(logits) == 1:
                    return ('긍정')
                elif np.argmax(logits) == 2:
                    return ('중립')