import numpy as np
import torch
import torch.nn as nn
from transformers import BertTokenizer, BertForMaskedLM
import chatgpt_sql
# Load pre-trained model (weights)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)

with torch.no_grad():
    model = BertForMaskedLM.from_pretrained('hfl/chinese-bert-wwm-ext').cuda()
    model.eval()
    # Load pre-trained model tokenizer (vocabulary)
    tokenizer = BertTokenizer.from_pretrained('hfl/chinese-bert-wwm-ext')
    all_chat = chatgpt_sql.selectAll()
    for row in all_chat:
        try:
            human_sentence = row['reply']
            tokenize_input = tokenizer.tokenize(human_sentence)
            tensor_input = torch.tensor([tokenizer.convert_tokens_to_ids(tokenize_input)])
            sen_len = len(tokenize_input)
            sentence_loss = 0.

            for i, word in enumerate(tokenize_input):
                # add mask to i-th character of the sentence
                tokenize_input[i] = '[MASK]'
                mask_input = torch.tensor([tokenizer.convert_tokens_to_ids(tokenize_input)]).cuda()

                output = model(mask_input)

                prediction_scores = output[0]
                softmax = nn.Softmax(dim=0)
                ps = softmax(prediction_scores[0, i]).log()
                word_loss = ps[tensor_input[0, i]]
                sentence_loss += word_loss.item()

                tokenize_input[i] = word
            human_ppl = np.exp(-sentence_loss/sen_len)

            ai_sentence = row['ai_reply']
            tokenize_input = tokenizer.tokenize(ai_sentence)
            tensor_input = torch.tensor([tokenizer.convert_tokens_to_ids(tokenize_input)])
            sen_len = len(tokenize_input)
            sentence_loss = 0.

            for i, word in enumerate(tokenize_input):
                # add mask to i-th character of the sentence
                tokenize_input[i] = '[MASK]'
                mask_input = torch.tensor([tokenizer.convert_tokens_to_ids(tokenize_input)]).cuda()

                output = model(mask_input)

                prediction_scores = output[0]
                softmax = nn.Softmax(dim=0)
                ps = softmax(prediction_scores[0, i]).log()
                word_loss = ps[tensor_input[0, i]]
                sentence_loss += word_loss.item()

                tokenize_input[i] = word
            ai_ppl = np.exp(-sentence_loss / sen_len)

            chatgpt_sql.updateppl(row['id'], human_ppl, ai_ppl)
        except Exception as e:
            print(e)
