from inference import inference,data_to_input
from flask import Flask, request, jsonify
from model.tokenization_kobert import KoBertTokenizer
import torch
from transformers import BertForTokenClassification
from tqdm import tqdm
import numpy as np
from postprocessing import dateProcess, timeProcess

app = Flask(__name__)

torch.set_flush_denormal(True)

# cpu/gpu 설정
device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')

# tokenizer 및 모델 설정
tokenizer = KoBertTokenizer.from_pretrained('monologg/kobert')
# print('----', tokenizer)
model = BertForTokenClassification.from_pretrained('monologg/kobert', num_labels = 8)
model.load_state_dict(torch.load('model_dict.pt',  map_location = device))

# label과 MAXLEN 설정
label_dict = {'0' : 0, 'terSfr': 1, 'terSto' : 2, 'date' : 3, 'time' : 4, 'arrTime' : 5, '[CLS]' : 6, '[SEP]' : 7 }
label_dict_decode = {v:k for k, v in label_dict.items()}
MAXLEN = 40

@app.route('/', methods = ['POST'])
def get_result():

    
    # print(request.is_json)
    params = request.get_json()
    # print(params['sentence'])

    # req_data = request.get_json()

    sentence = params['string']
    
    # sentence = request.args.get('sentence')
    input, attention_mask = data_to_input(sentence, tokenizer, MAXLEN)
    # print(sentence, attention_mask)
    result = inference(model, input, attention_mask, label_dict_decode, device, tokenizer)
    
    # print( '----------',result)
    
    return result


if __name__ == '__main__':
    
from inference import inference,data_to_input
from flask import Flask, request, jsonify
from model.tokenization_kobert import KoBertTokenizer
import torch
from transformers import BertForTokenClassification
from tqdm import tqdm
import numpy as np
from postprocessing import dateProcess, timeProcess

app = Flask(__name__)

# cpu/gpu 설정
device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')

# tokenizer 및 모델 설정
tokenizer = KoBertTokenizer.from_pretrained('monologg/kobert')
# print('----', tokenizer)
model = BertForTokenClassification.from_pretrained('monologg/kobert', num_labels = 8)
model.load_state_dict(torch.load('model_dict.pt',  map_location = device))

# label과 MAXLEN 설정
label_dict = {'0' : 0, 'terSfr': 1, 'terSto' : 2, 'date' : 3, 'time' : 4, 'arrTime' : 5, '[CLS]' : 6, '[SEP]' : 7 }
label_dict_decode = {v:k for k, v in label_dict.items()}
MAXLEN = 40

@app.route('/', methods = ['POST'])
def get_result():

    
    # print(request.is_json)
    params = request.get_json()
    # print(params['sentence'])

    # req_data = request.get_json()

    sentence = params['string']
    
    # sentence = request.args.get('sentence')
    input, attention_mask = data_to_input(sentence, tokenizer, MAXLEN)
    # print(sentence, attention_mask)
    result = inference(model, input, attention_mask, label_dict_decode, device, tokenizer)
    
    # print( '----------',result)
    
    return result


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
