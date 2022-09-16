import pandas as pd
import seq
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))
from model.tokenization_kobert import KoBertTokenizer


dataPATH = 'data/gen_data/data'
filePATH = 'data/gen_seq/data'

seq_in = []
seq_out = []
tokenizer = KoBertTokenizer.from_pretrained('monologg/kobert')

with open(dataPATH + '/data.txt', 'r', encoding = 'utf-8') as f:
    for sentence in f.readlines():
        slot_sentence = seq.get_slot(sentence)
        sentence = seq.pre_sentence(sentence)
        tokens = seq.get_seq_in(sentence, tokenizer)
        seq_in.append(' '.join(tokens))
        seq_out.append(' '.join(seq.get_seq_out(tokens, slot_sentence, tokenizer)))

data = pd.DataFrame(zip(seq_in, seq_out), columns = ['seq_in', 'seq_out'])


with open(filePATH+'/seq_in.txt', 'w', encoding = 'utf-8') as f:
    for line in seq_in:
        f.write(line+'\n')

with open(filePATH+'/seq_out.txt', 'w', encoding = 'utf-8') as f:
    for line in seq_out:
        f.write(line+'\n')