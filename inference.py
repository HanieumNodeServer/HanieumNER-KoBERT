import numpy as np
import torch
from transformers import BertForTokenClassification

from model.tokenization_kobert import KoBertTokenizer
from postprocessing import dateProcess, timeProcess

# input data 형식으로 바꾸기
def data_to_input(sentence, tokenizer, MAXLEN):
    #input 형식으로
    sentence = tokenizer.tokenize(sentence)
    sentence = ' '.join(sentence)
    sentence = tokenizer.convert_tokens_to_ids(('[CLS] ' + sentence + ' [SEP]').split())
    len_sentence = len(sentence)
    sentence += [0] * (MAXLEN - len_sentence)

    #attention_mask
    attention_mask = []
    attention_mask += [1] * len_sentence
    attention_mask += [0] * (MAXLEN - len_sentence)

    #tensor형식으로 변환
    sentence = torch.tensor(sentence).long()
    attention_mask = torch.tensor(attention_mask).long()

    return sentence, attention_mask

# 추론하기
def inference(model, input, attention_mask, label_dict_decode, device, tokenizer):
    # input 데이터 만들기
    input = input.to(device)
    attention_mask = attention_mask.to(device)
    
    model = model.to(device)
    model.eval()
    
    with torch.no_grad():
        output = model(input.reshape(1, 40), token_type_ids=None, attention_mask = attention_mask.reshape(1, 40))

    output = np.argmax(output[0].to('cpu').numpy(), axis = 2).reshape(40)
    input = tokenizer.convert_ids_to_tokens(input.to('cpu').numpy())

    
    arr = ''
    dep = ''
    date = ''
    dep_time = ''
    arr_time = ''
    
    for i, o in zip(input, output):
        o = label_dict_decode.get(o)
        
        if o == '[SEP]':
            return result

        if o == 'terSfr':
            arr += i.replace('▁', '')
        elif o == 'terSto':
            dep += i.replace('▁', '')
        elif o == 'date':
            date += i.replace('▁', '')
        elif o == 'time':
            dep_time += i.replace('▁', '')
        elif o == 'arrTime':
            arr_time += i.replace('▁', '')

        result = {'terSfr' : arr, 'terSto' : dep, 'date' : dateProcess(date), 'time' : timeProcess(dep_time), 'arrTime' : timeProcess(arr_time)}

